from scipy.fft import fft
import matplotlib.pyplot as plt
import numpy as np
sampling = 44100 #czę stotliwość
time = 5 #czas trwania wygenerowanego pliku
t = np.linspace(0,time,time*sampling) # wektor czasu uwzględniają cy zadaną
A = 0.1 # amplituda (od 0 do 1)
f = 440 # czę stotliwość w Hz
#data = A*np.sin(2*np.pi*f*t) #generuje przebieg
data = np.sign(A*np.sin(2*np.pi*f*t))
def TranformataFouriera(t,y):
    N = len(t)
    dt = t[1] - t[0]
    yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
    xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
    return xf, yf
xf, yf = TranformataFouriera(t,data) #obliczamy Transformatę Fouriera dla
plt.plot(xf, yf)
plt.xlim(0,3000) # ogranicza wykres do zakresu od 0 do 1kHz
plt.xlabel("frequency (Hz)")
plt.ylabel("amplitude")

plt.grid()
plt.show()