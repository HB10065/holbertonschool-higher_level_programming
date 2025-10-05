#!/usr/bin/python3
'''
Module Doc
'''


def read_file(filename=""):
    '''Function'''
    with open(filename, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        print('{}'.format(file_contents), end='')
