#!/bin/python3

import numpy as np
from matplotlib import pyplot as plt

def lcm(a,b):
    a_lcm = a
    b_lcm = b
    
    while a_lcm != b_lcm:
        if a_lcm > b_lcm:
            b_lcm += b
        else:
            a_lcm += a

    return a_lcm

def sin(f,fs,duration):
    samples = np.linspace(0, duration, int(fs*duration), endpoint=False)
    sine_samples = 32767 * np.sin(2*np.pi*f*samples)
    return np.int16(sine_samples)

def t_axis(fs, len_data):
    return np.linspace(0, len_data/fs, num=len_data)

def show_signal(data, fs):
    max_value = float(np.max(np.abs(data)))
    normalized_data = data / max_value

    plt.plot(t_axis(fs, len(normalized_data)),normalized_data)
    plt.title('Señal de Audio \'Modem Dialing\' ')
    plt.ylabel('Amplitud Normalizada')
    plt.xlabel('Tiempo (s)')
    plt.show()
    return None

def show_spectogram(data, fs):
    NFFT = 512 
    window = np.hamming(NFFT)
    plt.specgram(data, Fs=fs, window=window, NFFT=NFFT, noverlap=NFFT/2)
    plt.ylim(600,1800)
    # plt.xlim(10,13)
    plt.show()
    return None