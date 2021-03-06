# import libraries
import numpy as np
import scipy.signal as scpSig

class noiseGen:
    def __init__(self, fs, bw, tLen, tPw=[]):
        if not tPw:
            tPw = tLen / 1000.0
        self.fs = fs
        self.bw = bw
        self.nPw = int(np.round(tPw * fs))
        self.nPulses = int(np.round(tLen / tPw))
        self.nLen = self.nPw * self.nPulses
        self.hLpfA = []
        self.hLpfB = []
        
class noiseOne(noiseGen):
    def make_lpf(self):
        ripDb = 3.0
        stopDb = 30.0
        wFreq = self.bw / self.fs
        wStop = min((1 - wFreq) / 2 + wFreq, wFreq * 1.1)
        nLpf, WnArr = scpSig.cheb1ord(wFreq, wStop, ripDb, stopDb)
        self.hLpfB, self.hLpfA = scpSig.cheby1(nLpf, ripDb, WnArr)
    def make_sig(self):
        wNoise = np.random.random(self.nLen)
        wNoise = (wNoise - np.mean(wNoise)) / np.std(wNoise)
        if not len(self.hLpfB):
            self.make_lpf()
            ziNLen = max(len(self.hLpfB),len(self.hLpfA)) - 1
            self.zi = np.zeros(ziNLen)
        sigOut,self.zi = scpSig.lfilter(self.hLpfB, self.hLpfA, wNoise, zi=self.zi)
        return sigOut
        
        
        

