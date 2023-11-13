from enum import Enum

class carType(Enum):
    TRUCK = "ciezarowy"
    CAR = "osobowy"
    BIKE = 'jednoslad'


class Samochod:
    def __init__(self, numerRej, color, carType):
        self.numerRej = numerRej
        self.kolor = color;
        self.typ = carType;
        
    def wjazd(self, parking):
        return parking.wjazd(self)
    def wyjazd(self, parking):
        return parking.wyjazd(self)

    def printInfo(self):
        print(self.numerRej)
        print(self.kolor)
        print(self.typ.value)