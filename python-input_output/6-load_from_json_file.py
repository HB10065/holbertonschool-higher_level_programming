#!/usr/bin/python3
'''
Module Doc
'''
import json


def load_from_json_file(filename):
    '''Function'''
    with open(filename, 'r') as file:
        return json.load(file)
