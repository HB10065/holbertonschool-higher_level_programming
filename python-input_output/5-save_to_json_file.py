#!/usr/bin/python3
'''
Module Doc
'''
import json


def save_to_json_file(my_obj, filename):
    '''Function'''
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
