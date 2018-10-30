#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt

def t_axis(fs, len_data):
    return np.linspace(0,len_data/fs,num=len_data)

def main():
    filepath = 'modemDialing.wav'
    fs, data = wavfile.read(filepath)
    data = data / np.max(np.abs(data))

    plt.plot(t_axis(fs, len(data)),data)
    plt.title('Señal de Audio \'Modem Dialing\' ')
    plt.ylabel('Amplitud Normalizada')
    plt.xlabel('Tiempo (s)')
    plt.show()

if __name__ == "__main__":
    main()