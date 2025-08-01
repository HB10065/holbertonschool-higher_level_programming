#!/usr/bin/python3
'''
Module Doc
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Class Doc
    '''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
