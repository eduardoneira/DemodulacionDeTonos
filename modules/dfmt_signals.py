#!/bin/python3

from modules.utils import sin, digital_sin
import numpy as np

DEFAULT_FS = 8000
TIME_DIGIT = 0.07

POSSIBLE_FREQUENCIES = [697, 770, 852, 941, 1209, 1336, 1477, 1633]

DFMT_DIGITS =['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']

DFMT_SIGNALS = {
    '1': (697,1209),
    '2': (697,1336),
    '3': (697,1477),
    'A': (697,1633),
    '4': (770,1209),
    '5': (770,1336),
    '6': (770,1477),
    'B': (770,1633),
    '7': (852,1209),
    '8': (852,1336),
    '9': (852,1477),
    'C': (852,1633),
    '*': (941,1209),
    '0': (941,1336),
    '#': (941,1477),
    'D': (941,1633)
}

def nearest_possible_frequency(frequency):
    delta = 30

    for possible_frequency in POSSIBLE_FREQUENCIES:
        if frequency > possible_frequency - delta and frequency < possible_frequency + delta:
            return possible_frequency

    return None

def frequencies_to_digit(frequencies):
    for digit, digit_frequencies in DFMT_SIGNALS.items():
        if frequencies[0] == digit_frequencies[0] and frequencies[1] == digit_frequencies[1]:
            return digit

    return None

def dfmt_signal_for(digit, fs=DEFAULT_FS, duration=TIME_DIGIT, use_window=False):
    return sin(DFMT_SIGNALS[digit][0], fs, duration,use_window=use_window) + sin(DFMT_SIGNALS[digit][1], fs, duration,use_window=use_window)

def dfmt_generator_with(sequence, duration_digit=TIME_DIGIT):
    signal = np.array([])

    for digit in sequence:
        if signal.size > 0:
            signal = np.concatenate((signal, np.zeros(int(duration_digit*DEFAULT_FS))))

        signal = np.concatenate((signal,dfmt_signal_for(digit, duration=duration_digit)))

    return signal
