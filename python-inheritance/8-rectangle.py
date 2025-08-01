#!/usr/bin/python3
'''
Module Doc
'''
import importlib
base_geoemtry = importlib.import_module('7-base_geometry').BaseGeometry


class Rectangle(base_geoemtry):
    '''
    Class Doc
    '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.intger_validator('width', width)

        self.__width = width
        self.__height = height
