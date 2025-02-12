#!/usr/bin/python3
'''
MODULO
'''


def write_file(filename="", text=""):
    '''
    Funcion
    '''
    with open(filename, 'w') as t:
        t.write(text)

    return len(text)