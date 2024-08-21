# import objects
from utilsVbGenTest import *

def save_test():
    # import classes
    from tGens import noise5
    import uhd
    # set rf parameters
    fSamp = 61.44e6
    fCent = 1.0e9
    # instantiate noise source
    noiseObj = noise5(fs=fSamp, bw=10.0e6, tLen=0.010, tPw=1/4.0e5, nBins=64)
    # generate sig and plots
    sig = test_gen(noiseObj)
    #test_plot(sig, fs=fSamp, figId=4)
    # setup uhd and enable auto calibration
    usrp = uhd.usrp.MultiUSRP("type=b200")
    usrp.set_tx_dc_offset(True)
    usrp.set_tx_iq_balance(True)
    # transmit waveform from memory
    usrp.send_waveform(sig.astype(np.csingle), duration=30, freq=fCent, rate=fSamp, gain=30)

def test_noise():
    save_test()

if __name__ == "__main__":
    test_noise()
