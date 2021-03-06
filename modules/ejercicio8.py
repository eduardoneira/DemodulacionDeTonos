#!/bin/python3

import pdb
import numpy as np
from matplotlib import pyplot as plt
from modules.dfmt_signals import *
from modules.utils import show_signal,fft

def plot_digit_signal(idx, signal, magnitude, freq):
    plt.figure()
    plt.suptitle('Señal de dígito N°{}'.format(idx))

    plt.subplot(1, 2, 1)
    show_signal(DEFAULT_FS,signal,'Señal en el tiempo de dígito N°{}'.format(idx))

    plt.subplot(1, 2, 2)
    plt.plot(freq, magnitude)
    plt.title('FFT de dígito N°{}'.format(idx))
    plt.xlabel('Frequencia (Hz)')
    plt.ylabel('Módulo')
    # plt.savefig('img/ej8_FFT_{}.png'.format(idx),bbox_inches='tight')
    # plt.close()
    plt.show()

def decode_signal(signal):
    squared_signal = np.array(signal, dtype=np.float64) ** 2
    length_filter = 64
    moving_average_filter = np.ones(length_filter) / length_filter
    # show_signal(DEFAULT_FS, np.pad(moving_average_filter,(10,10),mode='constant'), 'Filtro Moving Average', normalized=False)
    # plt.savefig('img/ej8_moving_average_filter.png',bbox_inches='tight')
    # plt.close()
    energy = np.convolve(squared_signal, moving_average_filter)
    # plt.savefig('img/ej8_estimated_energy_delay.png',bbox_inches='tight')
    # plt.close()
    energy = energy[length_filter-1:]
    # show_signal(DEFAULT_FS, energy, 'Energia de la señal')
    # plt.show()

    # plt.savefig('img/ej8_estimated_energy.png', bbox_inches='tight')
    # plt.close()

    max_energy = np.max(energy)
    normalized_energy = energy / max_energy
    threshold = 0.1
    #show_signal(DEFAULT_FS, energy, 'Energia de la Señal')
    #show_signal(DEFAULT_FS, threshold*np.ones(len(energy)), 'Energia de la Señal', normalized=False)
    #plt.show()

    real_signal_index = np.where(normalized_energy > threshold)[0]

    diff_index = np.diff(real_signal_index)

    index_limits_signal = np.where(diff_index > 1)[0] + 1

    digit_intervals = np.split(real_signal_index, index_limits_signal)

    sequence = []

    for idx, digit_interval in enumerate(digit_intervals):
        current_signal = signal[digit_interval]
        magnitude, phase, freq = fft(DEFAULT_FS,current_signal)

        # plot_digit_signal(idx+1, current_signal, magnitude, freq)
        magnitude = magnitude[magnitude.size//2:]
        max_magnitude = np.max(magnitude)
        normalized_magnitude = magnitude / max_magnitude

        lobes_index = np.where(normalized_magnitude > 0.5)[0]
        
        lobes = []
        
        for lobe in lobes_index:
            frequency = lobe * 4000 / magnitude.size
            lobes.append(nearest_possible_frequency(frequency))  

        lobes = np.array(lobes)[lobes != np.array(None)]
        lobe_frequencies = np.unique(lobes)

        sequence.append(frequencies_to_digit(lobe_frequencies))

    return sequence

def ejercicio8(fs, data):
    # sequence_digits = ['3','2','3','2','7']
    sequence_digits = ['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']
    
    signal = dfmt_generator_with(sequence_digits)
    # signal += np.random.normal(0,1,len(signal))
    #show_signal(DEFAULT_FS, signal, 'Señal con Ruido Blanco Gaussiano')
    #plt.show()
    estimated_sequence = decode_signal(signal)

    print('Real sequence: {}'.format(sequence_digits))
    print('Estimated sequence: {}'.format(estimated_sequence))
