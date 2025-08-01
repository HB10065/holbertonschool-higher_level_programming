'''
Module Doc
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    Class Doc
    '''
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    '''
    Class Doc
    '''
    def sound(self):
        return 'Bark'

class Cat(Animal):
    '''
    Class Doc
    '''
    def sound(self):
        return 'Meow'
