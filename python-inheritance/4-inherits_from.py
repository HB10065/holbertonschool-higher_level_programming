#!/usr/bin/python3
'''
Module Doc
'''


def inherits_from(obj, a_class):
    '''
    Function inherits_from
    Arguments:
        obj: any object
        a_class: any Class
    return: True if obj is an instance sub-Class of a_class
            False otherwise
    '''
    return issubclass(obj, a_class)
