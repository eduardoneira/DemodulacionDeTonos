#!/bin/python3

import numpy as np
from modules.utils import show_signal, fft, t_axis
from modules.dfmt_signals import *
from matplotlib import pyplot as plt

def plot_pass_band_filters():
    plt.figure()
    plt.suptitle('Banco de Filtros Pasa Banda')

    for idx, frequency in enumerate(POSSIBLE_FREQUENCIES):
        pb_filter, fs = pass_band_filter(DEFAULT_FS, frequency)
        magnitude, angle, freq = fft(fs, pb_filter)
        plt.subplot(4,2,idx+1)
        plt.plot(freq, magnitude)
        plt.title('Filtro Pasa Banda para {} Hz'.format(frequency))
        plt.xlabel('Frequencia (Hz)')
        plt.ylabel('Modulo')

    #plt.savefig('img/ej9_pass_band_bank_filters.png', bbox_inches='tight')
    plt.show()


def pass_band_filter(fs, fc):
    quantity_samples = TIME_DIGIT * DEFAULT_FS
    duration = quantity_samples / fs 
 
    samples = np.linspace(-duration/2, duration/2, quantity_samples, endpoint=False)
  
    width_pulse = 60
    sinc = np.sinc(width_pulse*samples)
    
    sinc *= np.cos(2*np.pi*fc*samples)
    sinc *= np.hamming(len(sinc))
    return sinc, fs
    
    # show_signal(fs, sinc, 'Sinc')
    # plt.show()
    # plt.savefig('img/ej9_sinc_time_hamming_window.png', bbox_inches='tight')

    # magnitude, angle, freq = fft(fs, sinc)
    # plt.plot(freq, magnitude)
    # plt.title('DFT Sinc sin ventaneo')
    # plt.xlabel('Frequencia (Hz)')
    # plt.ylabel('Modulo')
    # plt.xlim(-50,50)
    # plt.show()
    # plt.savefig('img/ej9_sinc_dft_hamming_window.png', bbox_inches='tight')

def energy_estimator(signal):
    squared_signal = signal ** 2
    
    length_filter = 64
    moving_average_filter = np.ones(length_filter) / length_filter

    return np.convolve(squared_signal, moving_average_filter)

def plot_filter_bank(fs, data):
    y = {}

    plt.figure()
    plt.suptitle('Energía de corto tiempo para señal Y')
    # plt.suptitle('Señal Y filtrado por banco de filtros')

    for idx, frequency in enumerate(POSSIBLE_FREQUENCIES):
        pb_filter, fs_pbf = pass_band_filter(fs, frequency)

        y[frequency] = np.convolve(data, pb_filter)

        estimated_energy = energy_estimator(y[frequency])

        plt.subplot(4, 2, idx+1)
        plt.plot(t_axis(fs, len(estimated_energy)), estimated_energy)
        plt.title("Energía estimada para señal Y con pasa bandas {} Hz".format(frequency))
        # plt.title("Señal Y filtrada con pasa bandas {} Hz".format(frequency))
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Amplitud")

    plt.show()

def filter_bank(fs, data):
    energy_idxs_by_frequency = {}

    for frequency in POSSIBLE_FREQUENCIES:
        pb_filter, fs_pbf = pass_band_filter(fs, frequency)

        y = np.convolve(data, pb_filter)

        estimated_energy = energy_estimator(y)

        max_energy = np.max(estimated_energy)
        normalized_energy = estimated_energy / max_energy
        threshold = 0.6

        energy_idxs = np.where(normalized_energy > threshold)[0]

        energy_idxs_by_frequency[frequency] = []
        
        if energy_idxs.size > 0:
            diff_index = np.diff(energy_idxs)
            
            index_limits_signal = np.where(diff_index > 100)[0] + 1

            digit_intervals = np.split(energy_idxs, index_limits_signal)

            for digit_interval in digit_intervals:
                energy_idxs_by_frequency[frequency].append(digit_interval)

    sequence = []

    for low_freq in LOW_FREQUENCIES:
        for high_freq in HIGH_FREQUENCIES:
            for low_intervals_idxs in energy_idxs_by_frequency[low_freq]:
                for high_intervals_idxs in energy_idxs_by_frequency[high_freq]:
                    if np.intersect1d(low_intervals_idxs, high_intervals_idxs).size > 20:
                        sequence.append((low_intervals_idxs[0],frequencies_to_digit((low_freq,high_freq))))

    dtype = [('idx',int),('digit','S1')]
    sequence = np.array(sequence, dtype=dtype)
    sequence = np.unique(sequence)
    ordered_sequence = np.sort(sequence, order='idx')

    sequence = []
    for idx, digit in ordered_sequence:
        sequence.append(digit.decode('UTF-8'))

    return sequence

def ejercicio9():
    sequence_digits = ['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']
    signal = dfmt_generator_with(sequence_digits)
    #signal += np.random.normal(0,1,len(signal))
    #show_signal(DEFAULT_FS, signal, 'Señal con ruido')
    #plt.show()
    estimated_sequence = filter_bank(DEFAULT_FS, signal)

    print('Real sequence: {}'.format(sequence_digits))
    print('Estimated sequence: {}'.format(estimated_sequence))