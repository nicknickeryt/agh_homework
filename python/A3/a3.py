from samochod import Samochod
from samochod import carType 
from parking import Parking

#TODO check everything but should be fine
#######################
# Funkcja testująca
#  tworzy 6 obiektów i wykonuje kolejne kroki z instrukcji
#######################


def dummyTest():
    parking = Parking()


    # Tablice rejestracyjne mają na końcu pierwszą literę enumeratora typu samochodu dla ułatwienia debugowania
    samochod1 = Samochod("KR001C", "white", carType.CAR)
    samochod2 = Samochod("KR002C", "black", carType.CAR)
    samochod3 = Samochod("KR003T", "yellow", carType.TRUCK)
    samochod4 = Samochod("KR004T", "white", carType.TRUCK)
    samochod5 = Samochod("KR005B", "blue", carType.BIKE)
    samochod6 = Samochod("KR006B", "white", carType.BIKE)

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
    if(samochod6.wjazd(parking) == -2): print("Samochód 6 » Parking pełny!")	         # Sprawdzenie czy jest kod błędu, -2 oznacza, że nie ma wolnych miejsc

    # 11
    samochod1.wyjazd(parking)

    # 12
    samochod6.wjazd(parking)

    # 13
    parking.printStatus()

    # 14
    # Wyjazd wszystkich samochodów
    for car in parking.getCurrentVeh().copy():  # Lista musi być skopiowana do nowej, gdyż jest modyfikowana w pętli przez funkcję parking.wyjazd()
        car.wyjazd(parking)

    # 15
    parking.printStatus()

    # 16
    print("\nLista wszystkich numerow rej:")
    for car in parking.platesList:
        print("Numer rej: " + car.licensePlate)

    # 17
    print("\nLista wszystkich numerow rej samochodow ciezarowych:")
    for car in parking.platesList:
        if(car.carType == carType.TRUCK):
            print("Numer rej: " + car.licensePlate)

dummyTest()
