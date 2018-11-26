#!/bin/python3

from modules.utils import show_spectogram,fft
from matplotlib import pyplot as plt
import numpy as np

def save_fft_digit_signal(freq, magnitude, title):
    plt.plot(freq, magnitude)
    plt.title(title)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.xlim(650,1650)
    plt.savefig('img/ej6_FFT_{}.png'.format(title.lower().replace(' ','_')),bbox_inches='tight')
    plt.close()

def ejercicio6(fs, data):
    nfft = 512
    window = np.hamming(nfft)

    show_spectogram(fs, data, nfft, window,'Espectrograma \'Modem Dialing\' ')
    plt.ylim(600,1800)
    plt.xlim(3,5)
    plt.savefig('img/ej6_spectogram_zoom_digits.png', bbox_inches='tight')
    plt.close()

    first_digit = data[int(3.36*fs):int(3.45*fs)]
    magnitude, phase, freq = fft(fs, first_digit)
    save_fft_digit_signal(freq, magnitude, 'First digit')

    second_digit = data[int(3.52*fs):int(3.61*fs)]
    magnitude, phase, freq = fft(fs, second_digit)
    save_fft_digit_signal(freq, magnitude, 'Second digit')

    third_digit = data[int(3.67*fs):int(3.76*fs)]
    magnitude, phase, freq = fft(fs, third_digit)
    save_fft_digit_signal(freq, magnitude, 'Third digit')

    fourth_digit = data[int(3.83*fs):int(3.91*fs)]
    magnitude, phase, freq = fft(fs, fourth_digit)
    save_fft_digit_signal(freq, magnitude, 'Fourth digit')

    Fifth_digit = data[int(3.98*fs):int(4.06*fs)]
    magnitude, phase, freq = fft(fs, Fifth_digit)
    save_fft_digit_signal(freq, magnitude, 'Fifth digit')

