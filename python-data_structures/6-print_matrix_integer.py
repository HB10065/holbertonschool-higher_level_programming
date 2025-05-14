#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        rowlen = len(row)
        for column in row:
            if column == row[rowlen - 1]:
                print("{:d}".format(column), end='')
            else:
                print("{:d}".format(column), end=' ')
        print()
