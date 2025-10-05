#!/usr/bin/python3
'''
Module Doc
'''
import json


def serialize_and_save_to_file(data, filename):
    '''function'''
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    '''function'''
    with open(filename, "r") as file:
        return json.load(file)
