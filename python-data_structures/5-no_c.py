#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    idx = 0
    while len(my_string) <= idx:
        if my_string[idx] == 'c' or my_string[idx] == 'C':
            idx += 1
        new_str = new_str + my_string[idx]
    return new_str
