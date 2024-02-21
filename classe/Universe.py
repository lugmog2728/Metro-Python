from classe.Arret import *
from classe.Bus import *
from classe.Personne import *
from classe.Route import * 
from classe.Trajet import *
from module import FilesParser

class Universe: 
    def __init__(self, busFile, personneFile, routeFiles):
        self.arrets = []  #list(arret)
        self.routes = []  #list(route)
        self.graphe = {}  
        self.bus = []  #listBus
        self.personnes = [] #list(personnes)
        self.time = 0  #int
        self.initUniverse(busFile, personneFile, routeFiles)
        
        
    #---------------- init ----------------#
    def initRoutes(self, fileName):
        routes = FilesParser.parseFile(fileName)
        for route in routes: 
            arretA_name, arretB_name, distance = route
            arretA = self.find_arret(arretA_name)
            arretB = self.find_arret(arretB_name)
            route = Route(arretA, arretB, distance)
            self.routes.append(route)
            route = Route(arretB, arretA, distance)
            self.routes.append(route)
        return True
    
    def initBus(self, fileName):
        busS =  FilesParser.parseFile(fileName)
        for bus in busS:
            capacite_max, rapidite_chargement, vitesse_deplacement, parcours_names = bus
            busName = "Bus " + str(len(self.bus)+1)
            parcours = []
            for name in parcours_names: 
                arret = self.find_arret(name) 
                parcours.append(arret)
            bus = Bus(busName, capacite_max, rapidite_chargement, vitesse_deplacement, parcours)
            bus.calc_min_travel_times(self.graphe)
            self.bus.append(bus)
        return True

    def initPersonnes(self, fileName):
        personnes = FilesParser.parseFile(fileName)
        for personne in personnes:      
            for nb in range(0, int(personne[0]), 1):
                name = personne[1] + str(nb+1) 
                trajetA = Trajet(personne[2], self.find_arret(personne[3][0]), self.find_arret(personne[3][1]))
                trajetB = Trajet(personne[4], self.find_arret(personne[5][0]), self.find_arret(personne[5][1]))
                itineraireA = Personne.find_itineraire(trajetA, self.bus)
                itineraireB = Personne.find_itineraire(trajetB, self.bus)
                onePersonne = Personne(name, trajetA, trajetB, itineraireA, itineraireB)
                self.addPersonneToArret(onePersonne)
                self.personnes.append(onePersonne)
        return True
    
    def initUniverse(self, busFile, personneFile, routeFiles):
        self.initRoutes(routeFiles)
        self.addRoutesToArrets()
        self.makeGraphe()
        self.initBus(busFile)
        self.initPersonnes(personneFile)
        
        return True

    def addRoutesToArrets(self):
        for route in self.routes:
            route.arretA.routes.append(route)

    def addPersonneToArret(self, personne):
        arret = personne.trajet_aller.arret_dep
        arret.add_personne(personne)
        return True
    #---------------- Getter ----------------#
    def find_arret(self, name):
        for arret in self.arrets:
            if arret.name == name: 
                return arret
        arret = Arret(name)
        self.arrets.append(arret)
        return arret

    #---------------- timer ----------------#
    
    def tic(self):
        self.time += 1
        print(f"**************** Tic n°{self.time} ****************")
        for bus in self.bus:
            print(f"------- {bus.name} -------")
            bus.tic(self.time)
        return True
    
    def run(self, maxTime): #maxTime => int
        while self.time < maxTime:
            self.tic()
            if self.endRun():
                print(f"-------------------------FIN de la simulation au temps {self.time}---------------------")
                break
        for bus in self.bus:
            print(f"{bus.name} :  {len(bus.personnes)}")
        for arret in self.arrets:
            print(f"{arret.name} : {len(arret.file_attente)}")
        return True
    
    #---------------- action ----------------#
    def makeGraphe(self):
        graphe = {} 

        for route in self.routes:
            if route.arretA not in graphe:
                graphe[route.arretA] = []
            if route.arretB not in graphe:
                graphe[route.arretB] = []
            graphe[route.arretA].append((route.arretB, route.distance))
        self.graphe =  graphe
        return graphe

    def endRun(self):
        for bus in self.bus:
            if bus.personnes:
                return False

        for arret in self.arrets:
            if arret.file_attente:
                return False

        return True