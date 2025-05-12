#!/usr/bin/python3
def islower(c):
    low = 0
    upp = 0
    for i in range(ord('a'), ord('z') + 1):
        if c == chr(i):
            low += 1
    
    for i in range(ord('A'), ord('Z') + 1):
        if c == chr(i):
            upp += 1
    
    if upp == 0 and low == 0:
        return None
    elif low == 1:
        return True
    else:
        return False
