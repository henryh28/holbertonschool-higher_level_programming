#!/usr/bin/python3
"""
Divide a matrix argument (list of lists) by div and return
a new matrix with processed values
"""


def matrix_divided(matrix, div):
    """
    Divide matrix by div and return a new matrix with the processed values
    """
    answer = []
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_error)

        answer.append([round(element / div, 2) for element in row])

    return answer
