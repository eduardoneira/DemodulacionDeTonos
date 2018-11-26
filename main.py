#!/usr/bin/python3

from modules.utils import *
from scipy.io import wavfile

def main():
    filepath = 'modemDialing.wav'
    fs, data = wavfile.read(filepath)
    data = np.trim_zeros(data)

    show_signal(data, fs)
    show_spectogram(data, fs)
    
if __name__ == "__main__":
    main()