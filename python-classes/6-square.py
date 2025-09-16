#!/usr/bin/python3
'''
This module contains an empty class
'''


class Square():
    '''
    empty class
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    # Getters and Setters
    @property
    def size(self):
        '''getter of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter of size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''getter of position'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
        or not isinstance(value[0], int)\
        or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    # Methods
    def area(self):
        return self.__size ** 2

    def my_print(self):
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(' ', end='')

            for _ in range(self.__size):
                print('#', end='')
            print()

        if self.__size == 0:
            print()
