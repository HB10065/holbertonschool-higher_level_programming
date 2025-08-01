#!/usr/bin/python3
'''
Module Doc
'''


def inherits_from(obj, a_class):
    '''
    Function Doc
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
