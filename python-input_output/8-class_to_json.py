#!/usr/bin/python3
'''
Modulo
'''


import json


def class_to_json(obj):
    '''
    Funcion
    '''
    return (json.dumps(dir(obj)))