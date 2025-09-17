#!/usr/bin/python3
'''
This is a module with the class Rectangle
based on the contents of 4-rectangle.py
'''


class Rectangle():
    '''
    Class Rectangle
    private Attributes: width, height
    Methods:
        area: returns the area of the Rectangle
        perimeter: returns the perimeter of the Rectangle
        __str__: returns a string representation of the object
        __repr__: returns a string representation that can be used
                  to recreate the object
        __del__: prints a good bye when a rectangle is deleted
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # Getters and Setters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    # Methods
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            new_str = ''
            for i in range(self.__height):
                for _ in range(self.__width):
                    new_str += '#'
                if i != self.__height - 1:
                    new_str += '\n'

            return new_str

    def __repr__(self):
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

    def __del__(self):
        print('Bye rectangle...')
