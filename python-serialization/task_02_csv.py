#!/usr/bin/python3
'''Module Doc'''
import json, csv


def convert_csv_to_json(file_name):
    '''csv ro json'''
    try:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with ('data.json', 'w')as json_file:
            json.dump(data, json_file)
    
        return True

    except Exception:
        return False
