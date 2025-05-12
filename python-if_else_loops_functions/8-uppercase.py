#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str[i] in "abcdefghijklmnopqrstvwxyz":
            str[i] = ord(str[i]) + 33
    print("{}".format(str))
