#!/usr/bin/python3
'''
This module contains an empty class
'''


class Square():
    '''
    empty class
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''getter of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter of size'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2
