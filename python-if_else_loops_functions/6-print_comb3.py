#!/usr/bin/python3
for i in range(ord('0'), ord('8')):
    for j in range(ord('0') + int(chr(i)) + 1, ord('9') + 1):
        print('{}{}, '.format(chr(i), chr(j)), end='')
print('{}{}'.format(chr(i + 1), chr(j)))
