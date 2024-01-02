# INTRODUCTION

VbGen is a waveform simulation tool based on "Applied ECM: Vol. 2" by Leroy 
B. Van Brunt. This repo includes a PDF scan of the relevant sections in 
the book.  

The tool generates In-Phase / Quadrature-Phase (I/Q) data in the form of
output files containing noise jamming waveforms of various classes
(see Figure 152). Typically, this library pre-generates this data for
streaming to an Ettus USRP Software-Defined Radio (SDR) for RF playback. 
However, there is an option to save the data to a SigMF recording for 
playback via other means, e.g. Arbitrary Waveform Generator (AWG) or 
later analysis.  

# SETUP
Install Python 3 dependencies using following command in BASH terminal:  
`python3 -m pip install -r requirements.txt`  
Additionally, install developmental Ettus UHD drivers for Python 3 using following command in BASH terminal:  
`sudo apt install python3-uhd`  

# TESTS
The `tests` folder contains a number of example scripts for the following purposes:  
1. `vbGenIoTest.py` tests the file-writing utility of this library.  
2. `vbGenUhdTest.py` tests the UHD integration of this library with SDR devices.  
3. `vbGenWavTest.py` demodulates the waveforms for confirmation via signal analysis.   

# REFERENCES
NumPy Data Types (https://numpy.org/doc/stable/reference/arrays.dtypes.html)  
PySDR: USRP in Python (https://pysdr.org/content/usrp.html)  
Ettus UHD Manual: Python API (https://files.ettus.com/manual/page_python.html)  