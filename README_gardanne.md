# Python_metro 

Déveoppeur: Gardanne Lucas

## Context :
Ce projet a pour objecƟf de vous faire développer en langage Pyhton un programme qui va optimiser 
des déplacements de bus pour transporter des personnes.

## Qu'est ce qui marche?:  
    [X] main.py
    [X] Arret du programme si la limite de temps est passer ou tout les trajets fini
    [ ] Historique
        [ ] Sauvegarde de l'historique
        [ ] Navigation dans l'historique
    [X] Retour graphique

    - intialisation:  
        [X] Initalisation des arrets
        [X] Initalisation des routes
        [X] Initalisation des bus
        [X] Initalisation des personne
        [X] Initalisation de l'univer
        [ ] Gestion des donnée erroné

    - bus: 
        [X] Calcule de plus cour itineraire
        [X] Calcule de la position d'un bus sur une route
        [X] Mise ne mouvement d'un bus
        [X] Chargement et déchargement d'un bus
    
    -Personne :  
        [X] Calcule de l'itinéraire et des correspondance à empreinter
        [X] Gestion des départ
        [X] Gestion des montés/descentes d'une personne en fonction d'un arret ou d'un bus
        [ ] Gestion des arrivés simultanés
        [X] Une personne ne peux pas remonter directement dans le bus duquel elle descend

## remarque: 

    Malgré de nombreux tests, le programme n'arrive pas à aboutir. Après plus de 50 000 000 d'itérations, certaines personnes continuent d'essayer d'atteindre leur destination, même si une majorité a réussi à atteindre son objectif


## Complexitié de l'algorithme :

    Universe.py:
        - initPersonnes(self, fileName): 
            La complexité de cette fonction dépend du nombre de personnes présentes dans le fichier passé en paramètre et du nombre moyen d'itérations de la boucle interne pour chaque personne. La complexité évolue donc linéairement (O(n)) en fonction de ces facteurs.

        - initBus(self, fileName): 
            La complexité de cette fonction dépend du nombre de bus et du nombre d'arrêts définis dans le fichier passé en paramètre. En considérant les deux boucles "for" imbriquées, la complexité totale devient O(n * m), soit une complexité quadratique.

        - initRoute(self, fileName): 
            La complexité de cette fonction dépend du nombre de routes présentes dans le fichier passé en paramètre. On est donc en complexité O(n) car pour chaque route du fichier, il y a un nombre d'opérations interne similaire.

        - run(self, maxTime): 
            La complexité de cette fonction est linéaire (O(n)) par rapport à maxTime, représentée par la boucle while. Cette boucle continue jusqu'à ce que "self.time" atteigne "maxTime".
``````
    Bus.py:
        - tic(self, time): 
            La complexité de cette fonction dépend des complexités de "move", "dechargement", "chargement", "calc_time_next_step", et "next_arret". Si on considère ces fonctions individuellement comme étant de complexité constante (O(1)), alors la complexité totale de tic serait également constante (O(1) ) car les actions sont conditionnelles et déclenchent des fonctions de complexité constante.

        - chargement(self, time): 
            En considérant les opérations de complexité constante (par exemple, if personne in self.blacklist) et linéaire (par exemple, current_arret.file_attente.remove(personne)), la complexité de cette fonction serait, dans le pire des cas, O(n), où n est la taille de la liste current_arret.file_attente.

        - get_shortest_path(self, graphe, start, end): 
            Cette fonction utilisant l'algorithme de Dijkstra (plus court chemin), sa complexité est en moyenne O(a + n log(n)), où n est le nombre de nœuds dans le graphe et a le nombre d'arêtes.
``````
    Personne.py: 
        - find_itineraire(trajet, list_bus): 
            La complexité de cette fonction dépend de la taille de "list_bus" et de la structure des parcours des bus. Le premier bloc a une complexité de O(list_bus) * O(L), où L est le nombre de trajets du bus le plus long. Le deuxième bloc a une complexité de O(list_bus^2) * O(L).

        - want_take_this_bus(trajet, list_bus):
            Si l'on considère qu'il y a n itinéraires dans "itineraire_aller" ou "itineraire_retour", la complexité totale serait dans le pire des cas linéaire (O(n)).
