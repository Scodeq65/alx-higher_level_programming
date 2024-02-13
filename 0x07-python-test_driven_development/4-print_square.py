#!/usr/bin/python3
"""initialize a new square."""


def print_square(size):
    """"Print a square with the character #.

    Args:
        size (int): The size lenght of the square.

    Raises:
        TypeError: if size is not an integer or if size is a float.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
