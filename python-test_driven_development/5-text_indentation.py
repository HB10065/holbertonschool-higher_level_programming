#!/usr/bin/python3
'''
Module Doc
'''


def text_indentation(text):
    '''
    Function Doc
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = [":", "?", "."]
    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1

    current_line = ""

    while i < len(text):
        current_line += text[i]

        if text[i] in symbols:
            print(current_line.strip())
            print()
            current_line = ""

            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1

    if current_line:
        print(current_line.strip(), end="")