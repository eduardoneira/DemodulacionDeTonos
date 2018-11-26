#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile
from modules.ejercicio1 import ejercicio1
from modules.ejercicio2 import ejercicio2
from modules.ejercicio3 import ejercicio3

def read_wavfile():
    filepath = 'modemDialing.wav'
    fs, data = wavfile.read(filepath)
    return fs, np.trim_zeros(data)

def main():
    fs, data = read_wavfile()
    ejercicio3(fs, data)
    
if __name__ == "__main__":
    main()