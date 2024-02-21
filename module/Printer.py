def print_arret(arret):
    print(f"Arrêt {arret.name}")
    out = "- File d'attente: "
    for index, personne in enumerate(arret.file_attente):
        out += personne.name
        if index < len(arret.file_attente) - 1:
            out += ", "
    print(out)
    if arret.routes:
        print("Routes associées:")
        for route in arret.routes:
            print(f"- {route.arretA.name} --> {route.arretB.name} ({route.distance} m)")

def print_arrets(arrets):
    print("Les arrêts:")
    for arret in arrets:
        print_arret(arret)
        print("")

def print_bus(bus):
    print(f"{bus.name}: Capacité max: {bus.capacite_max}, Chargement: {bus.rapidite_chargement}, Vitesse: {bus.vitesse_deplacement}, en mouvement? : {bus.is_moving}, dernier arret: {bus.parcours[bus.index_next_arret][0][0].name}")
    print_parcours(bus.parcours)

def print_buss(buss):
    print("Les bus:")
    for bus in buss:
        print_bus(bus)
        print("")

def print_personne(personne):
    print(f"Personne: {personne.name}")
    print("Trajet aller:")
    print_trajet(personne.trajet_aller)
    print("Trajet retour:")
    print_trajet(personne.trajet_retour)
    print(f"itineraire aller: {personne.itineraire_aller}")
    print(f"itineraire retour: {personne.itineraire_retour}")
    

def print_personnes(personnes):
    print("Les personnes:")
    for personne in personnes:
        print_personne(personne)
        print("")

def print_route(route):
    print(f"- {route.arretA.name} --> {route.arretB.name} ({route.distance} m)")

def print_routes(routes):
    print("Les Routes:")
    for route in routes:
        print_route(route)
        print("")

def print_trajet(trajet):
    print(f"- a {trajet.heure_dep} va de {trajet.arret_dep.name} vers {trajet.arret_arr.name} ")

def print_universe(universe):
    print(f"Univers: {universe.time} tic")
    print_arrets(universe.arrets)
    print_routes(universe.routes)
    print_buss(universe.bus)
    print_personnes(universe.personnes)

def print_parcours(parcours):
    formatted_data = ""
    for index, (arrets, distance) in enumerate(parcours):
        arretA, arretB = arrets
        if(index == 0):
            formatted_data += f"{arretA.name} --> {arretB.name} ({distance} m)"
        else:
            formatted_data += f"{arretB.name} ({distance} m)"
        if index < len(parcours) - 1:
            formatted_data += " --> "
    print(formatted_data)

def print_graphe(graphe):
    for arret, voisins in graphe.items():
        voisins_str = [(voisin.name, distance) for voisin, distance in voisins]
        print(f"{arret.name}: {voisins_str}")
