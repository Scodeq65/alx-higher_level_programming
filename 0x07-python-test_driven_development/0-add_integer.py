#!/usr/bin/python3

"""
This module provides a function to add two integeres.
"""


def add_integer(a, b=98):
    """
    Add two integers.
    Args:
        a (int, float): the first integer.
        b (int, optional): The second integer. Defaults to 98.
    Returns:
        int: The sum of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
