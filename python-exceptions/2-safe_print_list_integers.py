#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        total_prints = 0
        for i in range(x):
            if type(my_list[i]) is int:
                print('{:d}'.format(my_list[i]), end='')
                total_prints += 1
            else:
                continue
        print()
        return total_prints
    except (IndexError, TypeError, ValueError):
        print()
        return total_prints
