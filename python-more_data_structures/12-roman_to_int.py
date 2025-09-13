#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_num = 0
    for c in reversed(roman_string):
        num = roman_numbers[c]
        if num < prev_num:
            total = total - num
        else:
            total = total + num
        prev_num = num

    return total
