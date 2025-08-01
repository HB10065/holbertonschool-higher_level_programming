#!/usr/bin/python3
'''
Module Doc
'''
import csv  
import json


def convert_csv_to_json(csv_filename):
    '''
    Function Doc
    '''
    try:
        with open(csv_filename, newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
