#!/usr/bin/python3
from calculator_1 import add as suma, sub as resta, mul as mult, div as divi


if __name__ == '__main__':
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, suma(a, b)))
    print('{} - {} = {}'.format(a, b, resta(a, b)))
    print('{} * {} = {}'.format(a, b, mult(a, b)))
    print('{} / {} = {}'.format(a, b, divi(a, b)))
