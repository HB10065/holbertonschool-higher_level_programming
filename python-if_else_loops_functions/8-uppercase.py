#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i in "abcdefghijklmnopqrstvwxyz":
            i = ord(i) - 32
        str2 += i
    print("{}".format(str2))
