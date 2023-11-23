from enum import Enum

class waveType(Enum):
    SIN = "Sinusoida"
    SQUARE = "Prostokątna"
    SAWTOOTH = "Piłoksztaltna"
    TRIANGLE = "Trójkątna"
    WHITE_NOISE = "Biały szum"

class csvType(Enum):
    TIME = "czas"
    FOURIER = "fourier"

class plotType(Enum):
    TIME = "czas"
    FOURIER = "fourier"

class props(Enum):
    SAMPLING = "czestotliwosc probkowania [Hz]"
    X0 = "poczatek zakresu czasu [s]"
    X1 = "koniec zakresu czasu [s]"
    FREQ = "czestotliwosc [Hz]"
    AMPLITUDE = "amplituda [m]"

class ops(Enum):
    DRAW_PLOT = "Narysuj wykres"
    DRAW_FOURIER = "Narysuj transformate Fouriera"
    WRITE_CSV_TIME = "Wpisz do .csv przebieg czasowy"
    WRITE_CSV_FOURIER = "Wpisz do .csv transformatę Fouriera"
    WRITE_WAV = "Wpisz do .wav czas"