# import libraries
import matplotlib.pyplot as plt
import numpy as np

class testPlot:
    def make_all_plots(self, sigOrig):
        nLen = len(sigOrig)
        fig, ax = plt.subplots(4)
        self.make_amp(sigOrig, nLen, ax[0])
        self.make_phi(sigOrig, nLen, ax[1])
        self.make_freq(sigOrig, nLen, ax[2])
        self.make_fft(sigOrig, nLen, ax[3])
        
    def make_freq(self, sigOrig, nLen, ax):
        # generate freq vs time vector
        phiSig = np.unwrap(np.angle(sigOrig))
        freqSig = np.diff(phiSig) * self.fs / (2 * np.pi)
        # axis vector
        tAxis = self.make_time_plot(nLen)
        # plot
        ax.plot(tAxis, freqSig)
        ax.grid(True)
        ax.set_xlim(np.min(tAxis), np.max(tAxis))
        ax.set_title('Inst. Freq.')
        ax.set_ylabel('Freq, Hz')
        ax.set_xlabel('Time, sec')
        
    def make_phi(self, sigOrig, nLen, ax):
        # generate phase vs time vector (rads)
        phiSig = np.angle(sigOrig)
        phiSig = phiSig[0:-1]
        # axis vector
        tAxis = self.make_time_plot(nLen)
        # plot
        ax.plot(tAxis, phiSig)
        ax.grid(True)
        ax.set_xlim(np.min(tAxis), np.max(tAxis))
        ax.set_title('Inst. Phase')
        ax.set_ylabel('Phase, rad')
        ax.set_xlabel('Time, sec')
    
    def make_amp(self, sigOrig, nLen, ax, prec = 1.0 / pow(2, 16)):
        # generate amplitude vs time vector (dBm)
        ampSig = np.abs(sigOrig)
        # replace zero's with precision value
        ampSig[np.where(ampSig==0)] = prec
        ampSig = ampSig[0:-1]
        # modify vector from vrms to dBm scale
        ampSig = 20.0 * np.log10(ampSig) + 30
        # axis vector
        tAxis = self.make_time_plot(nLen)
        # plot
        ax.plot(tAxis, ampSig)
        ax.grid(True)
        ax.set_xlim(np.min(tAxis), np.max(tAxis))
        ax.set_title('Amplitude')
        ax.set_ylabel('Power, dBm')
        ax.set_xlabel('Time, sec')
        
    def make_fft(self, sigOrig, nLen, ax, prec = 1.0 / pow(2, 16)):
        # generate fft plot
        fftSig = np.abs(np.fft.fftshift(np.fft.fft(sigOrig)))
        # replace zero's with precision value
        fftSig[np.where(fftSig)==0] = prec
        # modify vector from vrms to dBm scale
        fftSig = 20.0 * np.log10(fftSig) - 20.0 * np.log10(nLen) + 30.0
        # axis vector
        fAxis = self.make_freq_plot(nLen)
        # plot
        ax.plot(fAxis, fftSig)
        ax.grid(True)
        ax.set_xlim(np.min(fAxis), np.max(fAxis))
        ax.set_title('FFT')
        ax.set_ylabel('PSD, dBm/Hz')
        ax.set_xlabel('Freq., Hz')
    
    def make_freq_plot(self, nLen):
        # create freq axis vector
        fAxis = np.linspace(-1, 1, nLen) * self.fs / 2
        return fAxis
    
    def make_time_plot(self, nLen):
        # create time axis vector
        tAxis = np.linspace(0, (nLen - 2) / self.fs, nLen - 1)
        return tAxis
        
    def __init__(self, figId, fs):
        self.figId = figId
        self.fs = fs
