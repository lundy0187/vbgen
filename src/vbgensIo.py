# import libraries
import numpy as np
import sigmf
from sigmf import SigMFFile
from sigmf.utils import get_data_type_str
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
        saveSig[0::2] = (np.real(sigOrig))
        saveSig[1::2] = (np.imag(sigOrig))
        saveSig = saveSig.astype(self.dataType)
        return saveSig
    
    def __init__(self, fileName, fc=0, fs=0, dataType='<f4'):
        self.fileName = fileName
        self.fc = fc
        self.fs = fs
        self.dataType = dataType

class grFile(fileIoPar):
    def write_data(self, sigOrig, nLen=[]):
        # cast data to appropriate data type and save binary
        finSig = self.int_iq(sigOrig, nLen)
        finSig.tofile(self.fileName + '.sigmf-data')
        # set sigmf data type to complex
        sigmf_dtype = 'c'+ get_data_type_str(finSig)[1::]
        # generate sigmf metadata header file
        meta = SigMFFile(
            data_file=self.fileName + '.sigmf-data',
            global_info = {
                SigMFFile.DATATYPE_KEY: sigmf_dtype,
                SigMFFile.SAMPLE_RATE_KEY: int(self.fs)
            }
        )
        # generate a capture key
        meta.add_capture(0, metadata={
        SigMFFile.FREQUENCY_KEY: int(self.fc),
        })
        # write header to disk
        meta.tofile(self.fileName + '.sigmf-meta')
        