#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return None

    for row in matrix:
        rowlen = len(row)
        for column in row:
            if column == row[rowlen - 1]:
                print("{:d}".format(column))
            else:
                print("{:d}".format(column), end=' ')
