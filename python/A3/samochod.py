from enum import Enum

class carType(Enum):
    TRUCK = "ciezarowy"
    CAR = "osobowy"
    BIKE = "jednoslad"


class Samochod:
    def __init__(self, licensePlate, color, carType):
        self.licensePlate = licensePlate
        self.color = color;
        self.carType = carType;
        
    def wjazd(self, parking):
        return parking.wjazd(self)
    def wyjazd(self, parking):
        return parking.wyjazd(self)

    def printInfo(self):
        print(self.licensePlate)
        print(self.color)
        print(self.carType.value)