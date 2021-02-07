# import libraries
import numpy as np
import warnings

class fileIoPar:
    def size_check(self, sigOrig, nLen=[]):
        if not nLen:
            nLen = len(sigOrig)
        elif nLen > len(sigOrig):
            nLen = len(sigOrig)
            warnings.warn("Requested length greater than available data")
        sigOrig = sigOrig[0:nLen]
        return sigOrig, nLen
    
    def int_iq(self, sigOrig, nLen):
        sigOrig, nLen = self.size_check(sigOrig, nLen)
        saveSig = np.zeros(2 * nLen)
        saveSig[0::2] = (np.real(sigOrig)).astype(self.dataType)
        saveSig[1::2] = (np.imag(sigOrig)).astype(self.dataType)
        return saveSig
    
    def __init__(self, fileName, dataType='float32'):
        self.fileName = fileName
        self.dataType = dataType

class grFile(fileIoPar):
    def write_data(self, sigOrig, nLen=[]):
        finSig = self.int_iq(sigOrig, nLen)
        finSig.tofile(self.fileName + '.bin')
        