#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print('{} '.format(len(sys.argv)), end='')
        print('argument:' if len(sys.argv) == 1 else 'arguments:')
        i = 1
        for arg in sys.argv[1:]:
            print('{}: {}'.format(i, arg))
            i += 1
    else:
        print('0 arguments.')
