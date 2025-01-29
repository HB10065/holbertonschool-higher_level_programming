#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx + 1 > len(my_list):
        return my_list

    for i in range(len(my_list)):
        if i == idx:
            for j in range(i, len(my_list)):
                my_list[j] = my_list[j + 1]
            my_list.remove(len(my_list) - 1)
            break
    return my_list
