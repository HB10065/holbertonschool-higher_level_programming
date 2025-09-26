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
    return: True if obj is an instance of a sub-Class
            of a_class(directly or indirectly)
            False otherwise
    '''
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    return False
