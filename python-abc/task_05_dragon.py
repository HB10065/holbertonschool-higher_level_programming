#!/usr/bin/env python3
'''
Module Doc
'''


class SwimMixin:
    '''
    Class Doc
    '''
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    '''
    Class Doc
    '''
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    '''
    Class Doc
    '''
    def roar(self):
        print("The dragon roars!")
