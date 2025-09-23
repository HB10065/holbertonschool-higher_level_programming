#!/usr/bin/python3
'''
Module Doc
'''


def is_same_class(obj, a_class):
    '''
    Function is_same_class
    Arguments:
        obj: any object
        a_class: any Class
    return: True if obj is an instance of a_class
            False otherwise
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
