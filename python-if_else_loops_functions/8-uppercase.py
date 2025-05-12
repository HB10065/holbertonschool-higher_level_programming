#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = str[i]
        if c.isupper():
            str[i] = ord(str[i]) + 33
    print(str)
