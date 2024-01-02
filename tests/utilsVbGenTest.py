# import objects
import sys
import os
sys.path.append(os.getcwd() + '/src/')
import numpy as np

def test_plot(sigOrig, fs, figId):
    from visPlots import testPlot
    plotObj = testPlot(figId, fs)
    plotObj.make_all_plots(sigOrig)

def test_gen(noiseObj):
    # generate noise signals and append together
    sig = []
    for sigInd in range(0,3):
        sig = np.append(sig, noiseObj.make_sig())
    return sig