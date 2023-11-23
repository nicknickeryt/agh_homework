import numpy as np
from enums import *
from wave import Waveform
import matplotlib.pyplot as plt
import scipy.io.wavfile
import pandas as pd
import utils

# TODO cleanup
# TODO time [s]
# TODO units

class Generator():
    def __init__(self, sampling, time):
        self.sampling = sampling
        self.time = time
        self.x = np.arange(0, self.time, 1/self.sampling)
    
    def getWaveform(self, wave):
        match(wave.waveType):
            case waveType.SIN:
                return wave.amp*np.sin(2*np.pi*wave.freq*self.x)
            case waveType.SQUARE:
                return wave.amp*np.sign(np.sin(2*np.pi*wave.freq*self.x))
            case waveType.SAWTOOTH:
                return wave.amp*scipy.signal.sawtooth(2*np.pi*wave.freq*self.x)
            case waveType.TRIANGLE:
                return wave.amp*scipy.signal.sawtooth(2*np.pi*wave.freq*self.x, 0.5)
            case waveType.WHITE_NOISE:
                return wave.amp*np.random.normal(0,1/self.sampling, len(self.x))

    def drawPlot(self, wave, x0, x1, plotType):
        y = self.getWaveform(wave)
        match(plotType):
            case plotType.FOURIER:
                xt, yt = utils.fourier(self.x, y)
                plt.plot(xt, yt)
                plt.title("Transformata fouriera dla: " + wave.waveType.value)
                plt.xlabel("częstotliwość [Hz]")
                plt.ylabel("amplituda [m]")
            case plotType.TIME:
                plt.xlim(x0, x1)
                plt.plot(self.x, y)
                plt.title("Przebieg czasowy dla: " + wave.waveType.value)
                plt.xlabel("czas [s]")
                plt.ylabel("amplituda [m]")
        plt.show()
        return 0

    def writeWav(self, wave):
        fileName = wave.waveType.value + ".wav"
        scipy.io.wavfile.write(fileName, self.sampling, self.getWaveform(wave))
        return fileName

    def writeCsv(self, wave, csvType):
        y = self.getWaveform(wave)
        x = self.x
        if(csvType == csvType.FOURIER): x, y = utils.fourier(self.x, y)

        data = {"t":x,"y":y} 
        dataframe = pd.DataFrame(data) 
        fileName = csvType.value + "_" + wave.waveType.value + ".csv"
        dataframe.to_csv(fileName , index=False, sep="\t")
        return fileName

    
def doOperation(wave, sampling, operation, x0, x1):
    generator = Generator(sampling, x1-x0) 
    match(operation):
        case ops.DRAW_PLOT:
            return(generator.drawPlot(wave, x0, x1, plotType.TIME))
        case ops.DRAW_FOURIER:
            return(generator.drawPlot(wave, x0, x1, plotType.FOURIER))
        case ops.WRITE_WAV:
            return(generator.writeWav(wave))
        case ops.WRITE_CSV_FOURIER:
            return(generator.writeCsv(wave, csvType.FOURIER))
        case ops.WRITE_CSV_TIME:
            return(generator.writeCsv(wave, csvType.TIME))



