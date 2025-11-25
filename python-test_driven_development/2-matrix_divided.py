#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or 
        not all(isinstance(row, list) for row in matrix) or
        len(matrix) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    control = 0
    for i in range(0, len(matrix)):
        size = len(matrix[i])
        if len(matrix[i]) != size:
            control = 1

    if control == 1: raise(TypeError("Each row of the matrix must have the same size"))
    if not isinstance(div, (int, float)): raise(TypeError("div must be a number"))
    if div == 0: raise(ZeroDivisionError("division by zero"))

    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)

    return new_matrix
