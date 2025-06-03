#!/usr/bin/python3
'''
Module Documentation
'''


def append_write(filename="", text=""):
    '''
    Function Documentation
    '''

    with open(filename, 'a') as file:
        file.write(text)

    return (len(text))
