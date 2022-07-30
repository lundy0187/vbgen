# import objects
import sys
import os
sys.path.append(os.getcwd() + '/source/')
import numpy as np

def test_plot(sigOrig, fs):
    from visPlots import testPlot
    plotObj = testPlot(1, fs)
    plotObj.make_all_plots(sigOrig)

def test_noise():
    from tGens import noise3
    fs = 10.0e6
    bw = 2.0e6
    tPw = 1/1.0e5
    noiseObj=noise3(fs,bw,0.0001,tPw)
    sig = []
    for sigInd in range(0,5):
        sig = np.append(sig, noiseObj.make_sig())
    return sig, fs
    
if __name__ == "__main__":
    sigOrig, fsOrig = test_noise()
    test_plot(sigOrig, fsOrig)