# import objects
from utilsVbGenTest import *

def noise1_test():
    # import noise class
    from tGens import noise1
    # instantiate noise source
    noiseObj=noise1(fs=10.0e6, bw=2.0e6, tLen=0.0004, tPw=1/1.0e6)
    # generate sig and plots
    sig = test_gen(noiseObj)
    test_plot(sig, fs=10.0e6, figId=1)

def noise2_test():
    # import noise class
    from tGens import noise2
    # instantiate noise source
    noiseObj=noise2(fs=10.0e6, bw=2.0e6, tLen=0.0004, tPw=1/1.0e6)
    # generate sig and plots
    sig = test_gen(noiseObj)
    test_plot(sig, fs=10.0e6, figId=2)

def noise3_test():
    # import noise class
    from tGens import noise3
    # instantiate noise source
    noiseObj=noise3(fs=10.0e6, bw=2.0e6, tLen=0.0004, tPw=1/1.0e5)
    # generate sig and plots
    sig = test_gen(noiseObj)
    test_plot(sig, fs=10.0e6, figId=3)

def noise4_test():
    # import noise class
    from tGens import noise4
    # instantiate noise source
    noiseObj=noise4(fs=10.0e6, bw=2.0e6, tLen=0.0004, tPw=1/1.0e5)
    # generate sig and plots
    sig = test_gen(noiseObj)
    test_plot(sig, fs=10.0e6, figId=4)

def noise5_test():
    # import noise class
    from tGens import noise5
    # instantiate noise source
    noiseObj=noise5(fs=10.0e6, bw=2.0e6, tLen=0.0004, tPw=1/4.0e5, nBins=16)
    # generate sig and plots
    sig = test_gen(noiseObj)
    test_plot(sig, fs=10.0e6, figId=5)

def test_noise():
    noise1_test()
    noise2_test()
    noise3_test()
    noise4_test()
    noise5_test()
    
if __name__ == "__main__":
    test_noise()