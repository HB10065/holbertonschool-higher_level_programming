#!/usr/bin/python3
'''
Module Doc
'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''Abstract class'''
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    '''Class'''
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    '''class'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height + self.__width) * 2


def shape_info(object):
    '''function'''
    print('{}'.format(object.area()))
    print('{}'.format(object.perimeter()))
