#!/usr/bin/python3
def uppercase(str):
    for a in str:
        print(
            '{}'.format(chr(ord(a) - 32) if ord(a) >= ord('a') and
            ord(a) <= ord('z') else a), end=''
        )
    print(f'')
