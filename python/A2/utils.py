from blocks.kula import Kula 
from blocks.czworoscian import Czworoscian
from blocks.ostroslup_prost import Ostroslup
from blocks.stozek import Stozek
from blocks.walec import Walec
from blocks.elipsoida import Elipsoida

from enum import Enum

from enums import reqs

###############################################################
# Definicje obietów
###############################################################
class blocks(Enum):
    KULA = Kula()
    CZWOROSCIAN = Czworoscian()
    OSTROSLUP = Ostroslup()
    STOZEK = Stozek()
    WALEC = Walec()
    ELIPSOIDA = Elipsoida()

###############################################################
# Wrapper do operacji na obiektach (bryłach)
#  return: wynik obliczeń
###############################################################
def get(block, operation):
    match(operation):
        case reqs.MASS:
            return block.getMass()
        case reqs.VOLUME:
            return block.getVolume()
        case reqs.AREA:
            return block.getArea()

###############################################################
# Definicje stringów
###############################################################  
blockList = [
    ("kula", blocks.KULA), 
    ("czworoscian foremny", blocks.CZWOROSCIAN), 
    ("ostrosłup prostokątny", blocks.OSTROSLUP), 
    ("stożek", blocks.STOZEK), 
    ("walec", blocks.WALEC), 
    ("elipsoida", blocks.ELIPSOIDA)]

operationList = [
    reqs.MASS,
    reqs.VOLUME,
    reqs.AREA]