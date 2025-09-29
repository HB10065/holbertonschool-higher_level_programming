#!/usr/bin/python3
'''
Module Doc
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''Abstract class'''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''Dog'''
    def sound(self):
        return 'Bark'


class Cat(Animal):
    '''Cat'''
    def sound(self):
        return 'Meow'
