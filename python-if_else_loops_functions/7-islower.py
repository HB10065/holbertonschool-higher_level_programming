#!/usr/bin/python3
def islower(c):
    low = 0
    for i in range(ord('a'), ord('z') + 1):
        if c == chr(i):
            low += 1
    if low == 1:
        return True
    else:
        return False
