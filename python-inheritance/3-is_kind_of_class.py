#!/usr/bin/python3
'''
Module Doc
'''


def is_kind_of_class(obj, a_class):
    '''
    Function is_kind_of_class
    Arguments:
        obj: any object
        a_class: any Class
    return: True if obj is an instance of a_class
            or an instance of a sub-Class of a_class
            False otherwise
    '''
    return isinstance(obj, a_class)
