#!/usr/bin/python3
'''
This moduel contains a class that inherits from BaseGeometry
from '7-base_geometry'
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Private Instance Attributes:
        __width
        __height
    '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
