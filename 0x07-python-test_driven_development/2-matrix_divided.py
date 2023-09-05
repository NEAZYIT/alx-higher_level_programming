#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
        if rows have different sizes,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row sizes
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate non-zero divisor
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    result = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        result.append(new_row)

    return result
