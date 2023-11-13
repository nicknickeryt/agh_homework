from samochod import Samochod
from samochod import carType 
from parking import Parking

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
print(parking.freePlaces)

# 6
samochod2.wjazd(parking)

# 7
samochod4.wjazd(parking)
print(parking.freePlaces)

# 8
print(samochod5.wjazd(parking))
print(parking.freePlaces)

# 9
parking.printStatus()

# 10
if(samochod6.wjazd(parking) == -1): print("Parking pełny!")

# 11
samochod1.wyjazd(parking)
print(parking.freePlaces)

# 12
samochod6.wjazd(parking)

print(parking.freePlaces)

# 13
parking.printStatus()

# 14

for car in parking.getCurrentVeh().copy():
    print(parking.wyjazd(car))

# 15
parking.printStatus()

# 16
for car in parking.listaNumerow:
    if(car.typ == carType.TRUCK):
        print("Numer rej: " + car.numerRej)


#uzupelnic klase o wybrane rzeczy, pola, pola statyczne, metody cos w tym stluy xD