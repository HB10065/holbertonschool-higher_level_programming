#!/usr/bin/python3
'''
Module Doc
'''


def read_file(filename=""):
    '''Function'''
    with open(filename, 'r') as file:
        file_contents = file.read()
        print('{}'.format(file_contents))
