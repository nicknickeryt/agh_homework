from samochod import carType

class Parking:
    def __init__(self):
        self.freePlaces = 5
        self.occupiedPlaces = 0;
        self.money = 0;
        self.platesList = []
        self.currentVeh = []
        
    def getCurrentVeh(self):
        return self.currentVeh

    def wyjazd(self, samochod):
        if(samochod not in self.currentVeh): return -1        # Sprawdzenie, czy samochód jest na parkingu

        self.freePlaces+=1
        self.occupiedPlaces-=1
        self.currentVeh.remove(samochod)

        match samochod.carType:
            case(carType.CAR):
                self.money+=10
            case(carType.TRUCK):
                self.money+=30
            case(carType.BIKE):
                self.money+=5

    def wjazd(self, samochod):
        
        if self.freePlaces == 0: return -2                     # Sprawdzenie, czy są wolne miejsca
        if samochod in self.currentVeh: return -1              # Sprawdzenie, czy samochód nie jest już na parkingu

        self.freePlaces-=1
        self.occupiedPlaces+=1
        if(samochod not in self.platesList): self.platesList.append(samochod)
        self.currentVeh.append(samochod)
    
    
    def printStatus(self):
        print("Zajete miejsca: " + str(self.occupiedPlaces))
        print("Utarg: " + str(self.money))
