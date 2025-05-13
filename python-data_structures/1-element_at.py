#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    
    if len(my_list) != idx + 1:
        return None
    
    element = my_list[idx]
    return (element)
