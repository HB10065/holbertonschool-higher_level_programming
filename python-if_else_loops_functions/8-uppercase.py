#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i in "abcdefghijklmnopqrstvwxyz":
            i = ord(i) + 33
    print("{}".format(str))
