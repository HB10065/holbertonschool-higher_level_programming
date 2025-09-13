#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        total_prints = 0
        for element in my_list:
            print('{}'.format(element), end='')
            total_prints += 1
        print()
        return total_prints
    except IndexError:
        print('x cannot be larger than the list')
