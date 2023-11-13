from utils import *

###############################################################
# Główna część
#  - wypisanie listy brył i operacji
#  - wybór i podawanie danych
#  - sprawdzenie poprawności danych (wybór i dane do operacji)
###############################################################

#TODO FIX stozek.py -> podaj wysokosc,a nie tworzaca

def init():
    try:
        for x in blockList:
            print("["+ str(blockList.index(x)+1) + "] " + x[0])           # Lista brył

        i = int(input("\n<i> Wybierz numer bryły\n» "))
        if(i not in range (1, len(blockList)+1)): raise ValueError        # Sprawdzenie poprawności danych (wybór z listy)
        block = blockList[i-1][1].value

        for x in operationList:                                           # Lista operacji
            print("["+ str(operationList.index(x)+1) + "] " + x.value)

        i = int(input("\n<i> Wybierz numer operacji\n» "))
        if(i not in range (1, len(operationList)+1)): raise ValueError    # Sprawdzenie poprawności danych (wybór z listy)
        operation = operationList[int(i-1)]

        for req in block.getRequirenments(operation):                     # Sprawdzenie wymaganych danych do danej operacji na bryle
            value = float(input("Podaj " + req.value + "\n» "))           # Prośba o podanie danej
            block.setProps(req, value)

        print("\n<i> Obliczono: " + operation.value + " " + str(round(get(block, operation), 2)) + "\n")
        askAgain()
    except KeyboardInterrupt:                                             # Możliwość wyjścia używając KeyboardInterrupt (Ctrl^C)
        return
    except:                                                               # Informacja o złej wartości
        print("\n<!> Podano niepoprawne dane. Sprawdź, czy podana wartość jest poprawną wartością liczbową.\n")
        init()
        return
    
###############################################################
# Zapytanie o ponowne uruchomienie programu
# (!) Jeśli użytkownik nic nie wpisze, pytamy jeszcze raz
###############################################################
def askAgain():
    again = input("<?> Czy chcesz dokonać kolejnych obliczeń?\n» ")
    match again:
        case "tak":
            init()
        case "nie":
            return
        case _:
            askAgain()

init()