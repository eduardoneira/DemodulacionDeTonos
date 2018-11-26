#!/bin/python3

import numpy as np
from fractions import Fraction
from modules.dfmt_signals import *

def ejercicio5():
    factor = Fraction(1, 4000)

    for digit, frequencies in DFMT_SIGNALS.items():
        factor_a = factor * frequencies[0]
        factor_b = factor * frequencies[1]

        print('Digit {}  => pi*{}/{}, pi*{}/{}'.format(digit, factor_a.numerator, factor_a.denominator, factor_b.numerator, factor_b.denominator))
