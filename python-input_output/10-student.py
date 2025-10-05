#!/usr/bin/python3
'''
Module Doc
'''


class Student():
    '''Class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Methods
    def to_json(self, attrs=None):
        if (
            isinstance(attrs, list) and
            all(isinstance(element, str) for element in attrs)
            ):
            attributes = {
                key: getattr(self, key) for key in attrs
                if hasattr(self, key)
            }
            return attributes
        return self.__dict__
