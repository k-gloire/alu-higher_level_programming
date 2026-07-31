#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

This module provides matrix_divided, which returns a new matrix with
every element divided by a given number and rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix: a list of lists of ints or floats, all rows the same
            length.
        div: an int or float, the divisor. Must not be zero.

    Returns:
        A new matrix with every element divided by div and rounded to
        2 decimal places. The original matrix is left unchanged.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0 or not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of "
                "integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
