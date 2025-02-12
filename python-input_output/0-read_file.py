#!/usr/bin/python3
'''
MODULO
'''


def read_file(filename=""):
    '''
    Funcion
    '''
    with open(filename, 'r') as t:
        print(t.read())
