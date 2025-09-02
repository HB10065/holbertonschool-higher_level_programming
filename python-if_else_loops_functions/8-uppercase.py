#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print('{}'.format(c) if ord(c) >= ord('A') and
              ord(c) <= ord('Z') else 
              '{}'.format(chr(ord(c) + 32)), end='')
    print()
