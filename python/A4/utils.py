import numpy as np
from scipy.fft import fft
from enums import *

def fourier(t,y):
    N = len(t)
    dt = t[1] - t[0]
    yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
    xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
    return xf, yf

