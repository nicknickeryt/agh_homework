from samochod import carType

class Parking:
    def __init__(self):
        self.freePlaces = 5
        self.occupiedPlaces = 0;
        self.utarg = 0;
        self.listaNumerow = []
        self.currentVeh = []
    def getCurrentVeh(self):
        return self.currentVeh

    def wyjazd(self, samochod):
        if(samochod not in self.currentVeh): return -1

        self.freePlaces+=1
        self.occupiedPlaces-=1
        # self.listaNumerow.remove(samochod)
        self.currentVeh.remove(samochod)

        match samochod.typ:
            case(carType.CAR):
                self.utarg+=10
            case(carType.TRUCK):
                self.utarg+=30
            case(carType.BIKE):
                self.utarg+=5

    def wjazd(self, samochod):
        #TODO check for double entry in listaNumerow
        #TODO deny wjazd if already in, deny wyjazd if already out
        
        if(self.freePlaces == 0): return -1
        if(samochod in self.currentVeh): return -1

        self.freePlaces-=1
        self.occupiedPlaces+=1
        self.listaNumerow.append(samochod)
        self.currentVeh.append(samochod)
    
    
    def printStatus(self):
        print("Occupied places: " + str(self.occupiedPlaces))
        print("Utarg: " + str(self.utarg))