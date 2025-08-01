#!/usr/bin/python3
'''
Module Doc
'''
base_geoemtry = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_geoemtry):
    '''
    Class Doc
    '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
