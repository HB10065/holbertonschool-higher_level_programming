#!/usr/bin/python3
def uppercase(str):
    str2 = ''
    for i in str:
        if i in "abcdefghijklmnopqrstvwxyz":
            i = chr(ord(i) - 32)
        str2 = str2 + i
    print("{}".format(str2))
