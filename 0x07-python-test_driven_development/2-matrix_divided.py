#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the elements of the matrix.

    Returns:
        list of lists: A new matrix with elements divided by the divisor.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               if each row of matrix doesn't have the same size,
               or if div is not a number (integer or float).
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/float")

    row_size = len(matrix[0])
    for row in matrix:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/float")
        if len(row) != row_size:
            raise TypeError("Each of row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")
    if div == 0:
        raise ZeroDivision("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]
