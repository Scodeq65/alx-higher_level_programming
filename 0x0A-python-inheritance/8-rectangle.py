#!/usr/bin/python3
"""Module defining a class BaseGeometry."""


class BaseGeometry:
    """Empty class BaseGeometry."""

    def area(self):
        """Raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implement")

    def integer_validator(self, name, value):
        """Validates value as an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializing a rectangle with width and height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
