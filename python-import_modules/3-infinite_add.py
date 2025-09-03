#!/usr/bin/python3
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = 0
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])

        print('{}'.format(result))
    else:
        print('0')
