#!/usr/bin/python3
'''
Module Documentation
'''


class Square:
    '''
    Class that represents a square

    Attributes:
    size: a private attribute representing
        the size of the square
    '''
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end='')
                print()

    def area(self):
        return self.__size * self.__size
