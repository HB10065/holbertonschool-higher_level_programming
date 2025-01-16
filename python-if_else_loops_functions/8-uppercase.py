#!/usr/bin/python3
def islower(c):
    for i in range(ord('A'), ord('Z') + 1):
        if i == ord(c):
            return True
    return False
