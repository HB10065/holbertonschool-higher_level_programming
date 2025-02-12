#!/usr/bin/python3
'''
Modulo
'''


import json


def load_from_json_file(filename):
    '''
    Funcion
    '''
    with open(filename, 'r') as t:
        return json.loads(t.read())
