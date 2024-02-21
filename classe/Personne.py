from module import Printer

class Personne:
    def __init__(self, 
                 name, #str
                 trajet_aller, #Trajet
                 trajet_retour, #Trajet
                 itineraire_aller, 
                 itineraire_retour): 
        self.name = name
        self.trajet_aller = trajet_aller
        self.trajet_retour = trajet_retour
        self.itineraire_aller = itineraire_aller
        self.itineraire_retour = itineraire_retour
        self.quel_trajet = 'aller'

    @staticmethod
    def find_itineraire(trajet, list_bus):
        arret_depart = trajet.arret_dep
        arret_arrivee = trajet.arret_arr
        correspondances = []

        #vérifi si c'est possible en 1 bus
        for bus in list_bus:
            temp = [False, False]
            for trajet, distance in bus.parcours:
                (arret1, arret2) = trajet
                if arret1 == arret_depart:
                    temp[0] = True
                if arret1 == arret_arrivee:
                    temp[1] = True
            if temp[0] and temp[1]:
                correspondance_trouvee = True
                return [bus.name, arret_depart.name, arret_arrivee.name]          
            
        #vérifi si c'est possible en 2 bus
        for i in range(len(list_bus)):
            for j in range(len(list_bus)):
                bus1 = list_bus[i]
                bus2 = list_bus[j]
                temp = [False, False]
                bus1Arret=[]
                bus2Arret=[]
       
                # Vérification si la combinaison de deux bus permet d'atteindre aller_arret depuis arret_depart 
                for trajet, distance in bus1.parcours:
                    (arret1, arret2) = trajet
                    bus1Arret.append(arret1.name)
                    if arret1 == arret_depart:
                        temp[0] = True
                    if arret1 == arret_arrivee:
                        temp[1] = True
                for trajet, distance in bus2.parcours:
                    (arret1, arret2) = trajet
                    bus2Arret.append(arret1.name)
                    if arret1 == arret_depart:
                        temp[0] = True
                    if arret1 == arret_arrivee:
                        temp[1] = True
                if temp[0] and temp[1]:
                    correspondance = set(bus1Arret) & set(bus2Arret)
                    if(correspondance != None):
                        correspondances.append([bus1.name, arret_depart.name, list(correspondance)[0]])
                        correspondances.append([bus2.name, list(correspondance)[0], arret_arrivee.name])
                        return correspondances
        return None
    
    def want_take_this_bus(self, bus_name):
        if self.quel_trajet == 'aller':
            for trajet in self.itineraire_aller:
                if bus_name in trajet:
                    return True
            return False
        if self.quel_trajet == 'retour':
            for trajet in self.itineraire_retour:
                if bus_name in trajet:
                    return True
            return False
        return False 
    
    def want_stop_here(self, arret_name):
        if self.quel_trajet == 'aller':
            for trajet in self.itineraire_aller:
                if arret_name in trajet:
                    return True
            return False
        if self.quel_trajet == 'retour':
            for trajet in self.itineraire_retour:
                if arret_name in trajet:
                    return True
            return False
        return False 
    
    def isGoal(self, arret_name):
        
        if self.quel_trajet == 'aller':
            if len(self.itineraire_aller) == 1: 
                print('ici') 
                if self.itineraire_aller[-1] == arret_name : 
                    self.quel_trajet = "retour"
                    print("/////////////////////////retour///////////////////////")
            else:  
                if self.itineraire_aller[-1][-1] == arret_name : 
                    print('là')
                    self.quel_trajet = "retour"
                    print("/////////////////////////retour///////////////////////")
            return 
                
        if self.quel_trajet == 'retour':
            if len(self.itineraire_retour) == 1: 
                if self.itineraire_retour[-1] == arret_name : 
                    self.quel_trajet = "fini"
                    print("/////////////////////////FINI///////////////////////")
            else: 
                if self.itineraire_retour[-1][-1] == arret_name : 
                    self.quel_trajet = "fini"
                    print("/////////////////////////FINI///////////////////////")
            return True
        return False