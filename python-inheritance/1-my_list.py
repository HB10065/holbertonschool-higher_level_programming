#!/usr/bin/python3
'''
This Module contains the first exercise
about inheritance in python
'''


class MyList(list):
    '''
    Class MyList
    Public Methods:
        print_sorted: prints itself in ascending order
    '''

    def print_sorted(self):
        print(sorted(self))

