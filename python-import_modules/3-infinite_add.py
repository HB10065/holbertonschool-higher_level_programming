#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        suma = int(sys.argv[1])
        i = 1
        for arg in sys.argv[1:-1]:
            suma += int(sys.argv[i + 1])
            i += 1
        print('{}'.format(suma))
    else:
        print('0')
