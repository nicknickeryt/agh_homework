from samochod import Samochod
from samochod import carType 
from parking import Parking

#TODO check everything but should be fine

def dummyTest():
    parking = Parking()

    samochod1 = Samochod("KR001O", "white", carType.CAR)
    samochod2 = Samochod("KR002O", "black", carType.CAR)
    samochod3 = Samochod("KR003C", "yellow", carType.TRUCK)
    samochod4 = Samochod("KR004C", "white", carType.TRUCK)
    samochod5 = Samochod("KR005J", "blue", carType.BIKE)
    samochod6 = Samochod("KR006J", "white", carType.BIKE)

    # 1 
    samochod1.wjazd(parking)

    # 2
    samochod2.wjazd(parking)

    # 3
    samochod3.wjazd(parking)

    # 4
    samochod2.wyjazd(parking)

    # 5
    print("Wolne miejsca: " + str(parking.freePlaces))

    # 6
    samochod2.wjazd(parking)

    # 7
    samochod4.wjazd(parking)

    # 8
    samochod5.wjazd(parking)

    # 9
    parking.printStatus()

    # 10
    if(samochod6.wjazd(parking) == -1): print("Parking pełny!")

    # 11
    samochod1.wyjazd(parking)

    # 12
    samochod6.wjazd(parking)

    # 13
    parking.printStatus()

    # 14
    for car in parking.getCurrentVeh().copy():
        parking.wyjazd(car)

    # 15
    parking.printStatus()

    # 16
    print("Lista wszystkich numerow rej:\n")
    for car in parking.platesList:
        print("Numer rej: " + car.licensePlate)

    # 17
    print("Lista wszystkich numerow rej samochodow ciezarowych:\n")
    for car in parking.platesList:
        if(car.carType == carType.TRUCK):
            print("Numer rej: " + car.licensePlate)

dummyTest()
