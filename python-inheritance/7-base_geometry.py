#!/usr/bin/python3
'''
This moduel contains a class based off of '6-base_geometry'
'''


class BaseGeometry():
    '''
    Public Instance Methods:
        area: not implemented yet
        integer_validator: Validates for int and greater than 0
    '''
    # Methods
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
