#!/usr/bin/python3
'''
This module has the lookup function
'''


def lookup(obj):
    '''
    argument: any object
    return: a list of all avaliable attributes
            and methods of the object
    '''
    return dir(obj)
