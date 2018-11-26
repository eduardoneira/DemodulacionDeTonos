#!/bin/python3

from fractions import Fraction
from modules.utils import lcm
from modules.dfmt_signals import *

def ejercicio1():
    print('Fundamental frequency for each digit')

    result = {}

    for digit, frequencies in DFMT_SIGNALS.items():
        result[digit] = lcm(Fraction(1,frequencies[0]),
                            Fraction(1,frequencies[1]))

        print('{}  =>  {}/{}'.format(digit, result[digit].denominator, result[digit].numerator))

    return result