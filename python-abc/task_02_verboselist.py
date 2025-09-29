#!/usr/bin/python3
'''
Module Doc
'''


class VerboseList(list):
    '''Class'''
    def append(self, object):
        super().append(object)
        print('Added [{}] to the list.'.format(object))
        return None

    def extend(self, iterable):
        super().extend(iterable)
        print('Extended the list with [{}] items.'.format(
            len(iterable)))
        return None

    def remove(self, value):
        print('Removed [{}] from the list.'.format(value))
        return super().remove(value)

    def pop(self, index = -1):
        print('Popped [{}] from the list.'.format(self[index]))
        return super().pop(index)
