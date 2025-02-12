#!/usr/bin/python3
'''
Modulo
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    Funcion
    '''
    with open(filename, 'w') as t:
        t.write(json.dumps(my_obj))
