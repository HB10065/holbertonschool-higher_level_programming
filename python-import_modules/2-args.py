#!/usr/bin/python3
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('{} '.format(len(sys.argv) - 1), end='')
        print('arguments:' if len(sys.argv) != 2 else 'argument:')

        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]))
    else:
        print('0 arguments.')
