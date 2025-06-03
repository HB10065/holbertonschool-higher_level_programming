#!/usr/bin/python3
'''
Module Documentation
'''


def read_file(filename=""):
    '''
    Function Documentation
    '''

    with open(filename, 'r') as file:
        text = file.read()
    print('{}'.format(text), end='')
