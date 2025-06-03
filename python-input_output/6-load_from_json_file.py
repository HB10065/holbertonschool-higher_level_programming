#!/usr/bin/python3
'''
Module Documentation
'''
import json


def load_from_json_file(filename):
    '''
    Function Documentation
    '''

    with open(filename, 'r') as file:
        obj = json.loads(file.read())
    return obj
