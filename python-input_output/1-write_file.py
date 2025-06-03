#!/usr/bin/python3
'''
Module Documentation
'''


def write_file(filename="", text=""):
    '''
    Function Documentation
    '''

    with open(filename, 'w') as file:
        file.write(text)

    return (len(text))
