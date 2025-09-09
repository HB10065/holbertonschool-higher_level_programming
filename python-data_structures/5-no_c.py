#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for c in my_string:
        if ord(c) == ord('c') or ord(c) == ord('C'):
            continue
        else:
            new_string += c

    return new_string
