#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    i = 0
    while i < len(my_list):
        if i == idx:
            i += 1
            continue
        new_list = new_list + my_list[i]
    return new_list
