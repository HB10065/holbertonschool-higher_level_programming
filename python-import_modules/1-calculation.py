#!/usr/bin/python3
def main():
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    print('10 + 5 = {}'.format(add(a, b)))
    print('10 - 5 = {}'.format(sub(a, b)))
    print('10 * 5 = {}'.format(mul(a, b)))
    print('10 / 5 = {}'.format(div(a, b)))
