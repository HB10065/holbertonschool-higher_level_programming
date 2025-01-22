#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    i = 0
    for arg in dir(hidden_4):
        if arg[0] != '_' and arg[1] != '_':
            print('{}'.format(arg))
