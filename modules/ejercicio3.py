#!/bin/python3

from modules.dfmt_signals import *
from modules.utils import show_signal,fft
from matplotlib import pyplot as plt

def show_fft_digit_signal(freq, magnitude, title):
    plt.plot(freq, magnitude)
    plt.title(title)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.savefig('img/FFT_{}.png'.format(title.lower().replace(' ','_')),bbox_inches='tight')
    plt.close()

def ejercicio3(fs, data):
    first_digit = data[int(3.36*fs):int(3.45*fs)]
    magnitude, phase, freq = fft(fs, first_digit)
    show_fft_digit_signal(freq, magnitude, 'First digit')

    second_digit = data[int(3.52*fs):int(3.61*fs)]
    magnitude, phase, freq = fft(fs, second_digit)
    show_fft_digit_signal(freq, magnitude, 'Second digit')

    third_digit = data[int(3.67*fs):int(3.76*fs)]
    magnitude, phase, freq = fft(fs, third_digit)
    show_fft_digit_signal(freq, magnitude, 'Third digit')

    fourth_digit = data[int(3.83*fs):int(3.91*fs)]
    magnitude, phase, freq = fft(fs, fourth_digit)
    show_fft_digit_signal(freq, magnitude, 'Fourth digit')

    Fifth_digit = data[int(3.98*fs):int(4.06*fs)]
    magnitude, phase, freq = fft(fs, Fifth_digit)
    show_fft_digit_signal(freq, magnitude, 'Fifth digit')

    magnitude, phase, freq = fft(fs, data)
    show_fft_digit_signal(freq, magnitude, 'Modem Dialing')

    # fig, ax = plt.subplots(nrows=4, ncols=4)
    # fig.subplots_adjust(hspace=0.5, wspace=0.5)
    
    # for i, digit in enumerate(DFMT_DIGITS):
    #     signal = dfmt_signal_for(digit)
    #     magnitude, phase, freq = fft(signal, DEFAULT_FS)
    #     current_ax = ax[int(i/4)][i%4]

    #     current_ax.plot(freq, magnitude)
    #     current_ax.set_title('Digit {} => {}, {}'.format(digit, DFMT_SIGNALS[digit][0], DFMT_SIGNALS[digit][1]))
    #     current_ax.set_xlabel('Frequency [Hz]')
    #     current_ax.set_ylabel('Magnitude')

    # plt.show()