from generator import *
from enums import *

def askAgain():
    again = input("<?> Czy chcesz dokonać kolejnych obliczeń?\n» ")
    match again:
        case "tak":
            init()
        case "nie":
            return
        case _:
            askAgain()

def init():
    try:
        waveList = []
        j = 0
        for x in waveType:
            j+=1
            waveList.append(x)
            print("["+ str(j) + "] " + x.value)
        i = int(input("\n<i> Wybierz numer sygnału\n» "))
        if(i not in range (1, j+1)): raise ValueError
        selectedWave = waveList[i-1]    

        propsList = []
        for x in props:
            propsList.append(float(input("\n<i> Podaj: " + x.value + "\n» ")))

        opsList = []
        j = 0
        for x in ops:
            j+=1
            opsList.append(x)
            print("["+ str(j) + "] " + x.value)
        i = int(input("\n<i> Wybierz numer operacji\n» "))
        if(i not in range (1, j+1)): raise ValueError  
        selectedOp = opsList[i-1]

    except ValueError:
        print("<!> Podano niepoprawne dane.")
        askAgain()
        return  
    
    sampling = propsList[0]
    x0 = propsList[1]
    x1 = propsList[2]
    freq = propsList[3]
    amplitude = propsList[4]

    wave = Waveform(selectedWave, freq, amplitude)
    ret = doOperation(wave, sampling, selectedOp, x0, x1)
    if(ret != 0): print("Plik wynikowy: ./" + ret)
    askAgain()
    
init()