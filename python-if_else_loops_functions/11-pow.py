#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    else:
        c = a
        for i in range(1,b):
            c = c * c
        return c