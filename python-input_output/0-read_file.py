#!/usr/bin/python3
'''
MODULO
'''


def read_file(filename=""):
    '''
    Funcion
    '''
    with open(filename, 'r'):
        print(filename.read())
