from classe.Arret import *
from classe.Bus import *
from classe.Personne import *
from classe.Route import *
from classe.Trajet import *
from classe.Universe import *

from module.FilesParser import *
from module.Printer import *


def main():
        univ = Universe("data/bus.txt", "data/personne.txt", "data/route.txt")
        univ.run(100000)
        
        return True
main()