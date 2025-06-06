#!/usr/bin/python3
'''
Module Documentation
'''


class Rectangle:
    '''
    class Rectangle documentation
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''width's getter and setter'''
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    '''height's getter and setter'''
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)
