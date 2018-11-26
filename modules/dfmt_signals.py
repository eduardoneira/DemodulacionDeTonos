#!/bin/python3

from modules.utils import sin

DEFAULT_FS = 8000
TIME_DIGIT = 0.07

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

def dfmt_signal_for(digit, fs=DEFAULT_FS, duration=TIME_DIGIT):
    return sin(DFMT_SIGNALS[digit][0], fs, duration,use_window=True) + sin(DFMT_SIGNALS[digit][1], fs, duration,use_window=True)
