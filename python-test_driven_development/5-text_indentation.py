#!/usr/bin/python3
'''
Module Doc
'''



def text_indentation(text):
    '''
    Function Doc
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_str = ''
    for c in text:
        new_str += c
        if c in '.?:':
            new_str += '\n\n'

    print(new_str.strip())
