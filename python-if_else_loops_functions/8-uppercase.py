#!/usr/bin/python3
def uppercase(str):
    str2 = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            str2 += chr(ord(c) - 32)
        else:
            str2 += c

    print('{}'.format(str2))
