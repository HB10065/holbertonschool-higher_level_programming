'''
Module Doc
'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''
    Class Doc
    '''
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    '''
    Class Doc
    '''
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('radius must be grater or equal to zero')
        
        self.__radius = abs(radius)

    def perimeter(self):
        return 2 * math.pi * self.__radius
    
    def area(self):
        return math.pi * (self.__radius ** 2)

class Rectangle(Shape):
    '''
    Class Doc
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height
    
    def area(self):
        return self.__height * self.__width

def shape_info(shape):
    '''
    Function Doc
    '''
    print(f'Area: {shape.area()}')
    print(f'Perimeter: {shape.perimeter()}')
