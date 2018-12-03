#!/bin/python3

import numpy as np
from scipy.signal import tf2zpk
from matplotlib import pyplot as plt
from modules.dfmt_signals import *
from modules.ejercicio9 import pass_band_filter
from modules.utils import fft

def plot_pole_zero_map():
    plt.figure()
    plt.suptitle('Banco de Filtros - Diagrama de polos y zeros')

    for idx, frequency in enumerate(POSSIBLE_FREQUENCIES):
        pb_filter, fs = pass_band_filter(DEFAULT_FS, frequency)

        denominator = np.zeros(len(pb_filter))
        denominator[0] = 1

        zeros, poles, gain = tf2zpk(pb_filter, denominator)

        plt.subplot(4,2,idx+1)
        plt.plot(np.real(zeros), np.imag(zeros), 'ob', markerfacecolor='None')
        plt.plot(np.real(poles), np.imag(poles), 'xb')
        plt.grid()
        plt.xlim([-1.5,1.5])
        plt.ylim([-1.5,1.5])
        plt.xlabel('Re(Z)')
        plt.ylabel('Im(Z)')
        plt.title('Diagrama de polos y ceros para pasabanda de {} Hz'.format(frequency))
        

    plt.show()

def plot_phase():
    plt.figure()
    plt.suptitle('Banco de Filtros - Fase de DFT')

    for idx, frequency in enumerate(POSSIBLE_FREQUENCIES):
        pb_filter, fs = pass_band_filter(DEFAULT_FS, frequency)

        magnitude, phase, freq = fft(fs, pb_filter)

        plt.subplot(4,2,idx+1)
        plt.plot(freq, phase)
        plt.xlim([frequency-50,frequency+50])
        plt.title('Filtro Pasa Banda para {} Hz'.format(frequency))
        plt.xlabel('Frequencia (Hz)')
        plt.ylabel('Fase')

    plt.show()

def ejercicio10():
    #plot_pole_zero_map()
    plot_phase()