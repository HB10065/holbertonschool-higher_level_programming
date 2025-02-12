#!/usr/bin/python3
'''
MODULO
'''


def append_write(filename="", text=""):
    '''
    Funcion
    '''
    with open(filename, 'a') as t:
        t.write(text)
    return len(text)
