#!/bin/python3

from scipy.io import wavfile
from modules.utils import sin

def ejercicio2(fs):
    signal = sin(800,fs,1) + sin(1200,fs,1)
    wavfile.write('output/DFMT_800_1200.wav',fs,signal)

