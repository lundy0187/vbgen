# import libraries
import numpy as np
import scipy.signal as scpSig

class noiseGen:      
    def __init__(self, fs, bw, tLen, tPw=[], nBins=16):
        if not tPw:
            tPw = tLen / 1000.0
        # define analog values
        self.fs = fs
        self.bw = bw
        self.tLen = tLen
        self.tPw = tPw
        # define digital values
        self.nPw = int(np.round(tPw * fs))
        self.nPulses = int(np.round(tLen / tPw))
        self.nLen = self.nPw * self.nPulses
        self.nBins = nBins
        # define placeholder objects
        self.hLpfA = []
        self.hLpfB = []
        self.modObj = []
        # residual parameters
        self.phVal = 0

    def comp_mod(self, freqVec, ampVec=[]):
        if not len(ampVec):
            ampVec = np.ones(self.nLen)
        phVec = 2.0 * np.pi * np.cumsum(freqVec) / self.fs
        sigOut = ampVec * np.exp(1j * phVec)
        return sigOut
        
class noise1(noiseGen):
    def make_lpf(self):
        ripDb = 3.0
        stopDb = 30.0
        wFreq = self.bw / self.fs
        wStop = min((1 - wFreq) / 2 + wFreq, wFreq * 1.1)
        nLpf, WnArr = scpSig.cheb1ord(wFreq, wStop, ripDb, stopDb)
        nLpf = min(nLpf, 9) # this implies a minimum frequency resolution
        self.hLpfB, self.hLpfA = scpSig.cheby1(nLpf, ripDb, WnArr)
    def make_sig(self):
        wNoise = np.random.random(self.nLen)
        wNoise = (wNoise - np.mean(wNoise)) / np.std(wNoise)
        if not len(self.hLpfB):
            self.make_lpf()
            ziNLen = max(len(self.hLpfB),len(self.hLpfA)) - 1
            self.zi = np.zeros(ziNLen)
        sigOut,self.zi = scpSig.lfilter(self.hLpfB, self.hLpfA, wNoise, zi=self.zi)
        sigOut = sigOut / np.std(sigOut)
        return sigOut

class noise2(noiseGen):
    def make_sig(self):
        if not self.modObj:
            self.modObj = noise1(self.fs, 1/self.tPw, self.tLen)
        freqVec = self.modObj.make_sig()
        freqVec = (1 / (1 + np.exp(-freqVec)) - 1/2) * 2
        freqVec = self.bw * freqVec / 2
        sigOut = self.comp_mod(freqVec)
        return sigOut
    
class noise3(noiseGen):
    def make_sig(self):
        proType = np.linspace(-1.0, 1.0 ,self.nPw) * self.bw / 2.0
        freqVec = np.tile(proType, self.nPulses)
        sigOut = self.comp_mod(freqVec)
        return sigOut

class noise5(noiseGen):
    def make_sig(self):
        proType = np.random.randint(0, self.nBins, self.nPulses)
        proType = (proType - self.nBins / 2) * self.bw / self.nBins
        freqVec = np.repeat(proType, self.nPw)
        sigOut = self.comp_mod(freqVec)
        return sigOut
        
        

