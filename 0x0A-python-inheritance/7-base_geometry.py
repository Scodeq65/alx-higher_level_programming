#!/usr/bin/python3
"""Module defining a class BaseGeometry."""


class BaseGeometry:
    """Empty class BaseGeometry."""

    def area(self):
        """Raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
