#!/usr/bin/python3
def uppercase(str):
    for a in str:
        print(f'{chr(ord(a) - 32) if ord(a) >= ord('a') and a <= ord('z') else a}', end='')
    print(f'')
