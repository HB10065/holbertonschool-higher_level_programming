#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        c = a
        for i in range(1, b):
            c = c * c
        return c
    else:
        c = 1 / a
        for i in range(1, -b):
            c = c * c
        return c
