from module.Printer import *
import math 

class Bus:
    def __init__(self,
                 name, #str
                 capacite_max,  #int
                 rapidite_chargement, #int
                 vitesse_deplacement,  #int
                 parcours): #list[Arret]  
        self.name = name
        self.capacite_max = int(capacite_max)
        self.rapidite_chargement = rapidite_chargement
        self.vitesse_deplacement = vitesse_deplacement
        self.parcours = parcours
        self.personnes = []
        self.index_next_arret = 0 #index de l'arret 
        self.is_moving = False 
        self.arrive_time = 0 
        self.phase = "dechargement"
        self.blacklist = []


    def tic(self, time):
        if self.is_moving:
            self.move(time)
        else:
            if self.phase == "dechargement": 
                self.dechargement(time)
            elif self.phase == "chargement":
                self.chargement(time)
            if self.is_moving: 
                self.calc_time_next_step(time)
                self.next_arret()
                self.move(time)
        return True

    def move(self, time):
        if(self.arrive_time == time):
            print(f"arrivé a l'Arret {self.parcours[self.index_next_arret][0][0]}")
            self.is_moving = False
            self.phase = "dechargement"
        else: 
            print(f"arrive dans {self.calc_position(time)} m")
    
    def chargement(self, time):
        if len(self.personnes) < self.capacite_max:
            current_arret = self.parcours[self.index_next_arret][0][0]
            for personne in current_arret.file_attente:
                if personne in self.blacklist:
                    continue 
                if personne.quel_trajet == "retour":
                    if int(personne.trajet_retour.heure_dep) < time:
                        continue               
                if personne.want_take_this_bus(self.name): 
                    self.personnes.append(personne)
                    print(f'-----------------------------------------{personne.name} monte')
                    current_arret.file_attente.remove(personne)
                    return  
        print('chargement fini')   
        self.is_moving = True  
        self.blacklist = []    
        return
    
    def dechargement(self, time): 
        current_arret = self.parcours[self.index_next_arret][0][0]
        for personne in self.personnes:
            if personne.want_stop_here(current_arret.name):
                self.personnes.remove(personne)
                print(f"----------------------------------------{personne.name} descends")
                if personne.isGoal(current_arret.name):
                    return 
                current_arret.file_attente.append(personne)
                self.blacklist.append(personne)
                   
                return
        self.phase ="chargement"
        print("déchargement fini")
        self.chargement(time)
        return

    def calc_position(self, time):
        return math.ceil((self.arrive_time-time)/int(self.vitesse_deplacement))
    
    def calc_time_travel(self, length):
        return length*int(self.vitesse_deplacement)
    
    def calc_time_next_step(self, time):
        travel_time = self.parcours[self.index_next_arret][1]
        self.arrive_time = time + travel_time
        return True
    
    def next_arret(self):
        if self.index_next_arret < len(self.parcours)-1 :
            self.index_next_arret += 1
        else:
            self.index_next_arret = 0
        return self.parcours[self.index_next_arret]
    
    def get_shortest_path(self, graphe, start, end):
        visited = []         
        distances = {arret : (None, 2**30) for arret in graphe}
        distances[start] = 0             
        len_graph = len(graphe)         
        current = start
        coefficient = 0
        
        while len(visited) < len_graph:
           
            visited.append(current)
            for neighbor in graphe[current]:
                arret = neighbor[0] 
                weight = neighbor[1]  
                if arret not in visited:
                    d = distances[arret][1]
                    if coefficient + int(weight) < d:
                        distances[arret] = (current, coefficient + int(weight))
            minimum = (None, 2**30)
            for arret in graphe:
                if  arret not in visited and distances[arret][1] < minimum[1]:
                    minimum = (arret, distances[arret][1])
            current, coefficient = minimum
        
        arret = end    
        length = distances[end][1]
        return length
        
    def calc_min_travel_times(self, graph):
        min_travel_times = {}  

        for i in range(len(self.parcours)):
            current_arret = self.parcours[i]
            next_arret = self.parcours[(i + 1) % len(self.parcours)]         
            shortest_path = self.get_shortest_path(graph, current_arret, next_arret)
            if shortest_path is not None:
                total_time = self.calc_time_travel(shortest_path)
                min_travel_times[(current_arret, next_arret)] = total_time
        self.parcours = list(min_travel_times.items())
        return min_travel_times