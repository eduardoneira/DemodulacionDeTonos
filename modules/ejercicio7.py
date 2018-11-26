#!/bin/python3

from scipy.io import wavfile
from modules.dfmt_signals import *
from modules.utils import show_signal,show_spectogram
from matplotlib import pyplot as plt
import numpy as np

def ejercicio7():
    sequence_digits = ['3','2','3','2','7']
    signal = dfmt_generator_with(sequence_digits)

    wavfile.write('output/DFMT_32327.wav',DEFAULT_FS,signal)
    show_signal(DEFAULT_FS, signal, 'Señal DMFT Autogenerada 3 2 3 2 7')
    plt.savefig('img/ej7_dmft_time_32327.png', bbox_inches='tight')

    nfft = 256
    window = np.hamming(nfft)
    show_spectogram(DEFAULT_FS,signal,nfft,window,title='Espectrograma DMFT Autogenerada 3 2 3 2 7')
    plt.savefig('img/ej7_dmft_specgram_32327.png', bbox_inches='tight')


