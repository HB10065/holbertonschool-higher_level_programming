#!/usr/bin/python3
'''
Module Documentation
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function Documentation
    '''

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
