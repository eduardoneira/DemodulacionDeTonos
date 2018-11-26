#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile
from modules.ejercicio1 import ejercicio1
from modules.ejercicio2 import ejercicio2

def read_wavfile():
    filepath = 'modemDialing.wav'
    fs, data = wavfile.read(filepath)
    data = np.trim_zeros(data)

    return fs, data

def main():
    ejercicio2(8000)
    
if __name__ == "__main__":
    main()