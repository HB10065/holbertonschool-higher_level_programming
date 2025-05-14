#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    for element in my_list:
        if element % 2 == 0:
            div_list = div_list + [True,]
        else:
            div_list = div_list + [False,]

    return div_list
