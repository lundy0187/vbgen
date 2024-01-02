# import objects
from utilsVbGenTest import *

def save_test():
    # import classes
    from tGens import noise5
    from vbgensIo import grFile
    # set rf parameters
    fSamp = 10.0e6
    fCent = 1.0e9
    # instantiate noise source
    noiseObj = noise5(fs=fSamp, bw=6.0e6, tLen=0.001, tPw=1/4.0e5, nBins=128)
    # generate sig and plots
    sig = test_gen(noiseObj)
    test_plot(sig, fs=fSamp, figId=4)
    # generate file
    fileWrite = grFile('data/noise5', fc=fCent, fs=fSamp, dataType='<f4')
    fileWrite.write_data(sig)

def test_noise():
    save_test()

if __name__ == "__main__":
    test_noise()