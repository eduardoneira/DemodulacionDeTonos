#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile
from modules.ejercicio1 import ejercicio1
from modules.ejercicio2 import ejercicio2
from modules.ejercicio3 import ejercicio3
from modules.ejercicio5 import ejercicio5
from modules.ejercicio6 import ejercicio6
from modules.ejercicio7 import ejercicio7
from modules.ejercicio8 import ejercicio8
from modules.ejercicio9 import ejercicio9
from modules.ejercicio10 import ejercicio10

def read_wavfile():
    filepath = 'modemDialing.wav'
    fs, data = wavfile.read(filepath)
    return fs, np.trim_zeros(data)

def main():
    fs, data = read_wavfile()
    ejercicio9(fs, data)
    
if __name__ == "__main__":
    main()