#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = my_list[0]
    for int in my_list:
        if max < int:
            max = int
    return max
