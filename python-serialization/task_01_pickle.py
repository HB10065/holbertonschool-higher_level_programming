#!/usr/bin/python3
'''
Module Doc
'''
import pickle


class CustomObject():
    '''class'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    # Methods
    def display(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Is student: {}'.format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
