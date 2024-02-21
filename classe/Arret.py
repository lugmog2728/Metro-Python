class Arret:
    def __init__(self, name): 
        self.name = name  #str
        self.file_attente = [] #list(personne)
        self.routes = []  #list(Route)
 
    def add_route(self, route): 
        self.routes.append(route)
    
    def add_personne(self, personne):
        self.file_attente.append(personne)
        
    def remove_personne(self, personne):
        self.file_attente.append(personne)
        
    def __str__(self) -> str:
        return self.name