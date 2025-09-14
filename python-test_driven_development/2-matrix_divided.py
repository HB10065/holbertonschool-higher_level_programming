#!/usr/bin/python3
def matrix_divided(matrix, div):
    for row in matrix:
        for element in row:
            if not isinstance(element, int) and\
                not isinstance(element, float):
                raise TypeError('matrix must be a matrix '
                '(list of lists) of integers/floats')

        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must '
            'have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
