#!/usr/bin/python3
'''
Module Documentation
'''
import sys


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
        new_list = []
        for i in range(1, len(sys.argv)):
            new_list = new_list + sys.argv[i]
    with open('add_item.json', 'w') as file:
        file.write(new_list)
