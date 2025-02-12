#!/usr/bin/python3
'''
MODULO
'''


def append_write(filename="", text=""):
    '''
    Funcion
    '''
    with open(filename, 'w') as t:
        t.a(text)
