#!/usr/bin/python3
'''
Module Documentation
'''
import sys
import json
import os


def load_from_json_file(filename):
    '''
    Function Documentation
    '''

    with open(filename, 'r') as file:
        obj = json.loads(file.read())
    return obj

def save_to_json_file(my_obj, filename):
    '''
    Function Documentation
    '''

    with open(filename, 'w') as file:
        json.dump(my_obj, file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists('add_item.json'):
            new_list = load_from_json_file('add_item.json')
        else:
            new_list = []

        for i in range(1, len(sys.argv)):
            new_list.append(sys.argv[i])
    save_to_json_file(new_list, 'add_item.json')
