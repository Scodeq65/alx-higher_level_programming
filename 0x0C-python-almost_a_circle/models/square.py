#!/usr/bin/python3
"""This module defines the Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Sqr, which is a special case of a rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.
        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square's position.
            y (int): The y coordinate of the square's position.
            id (int): The identifier of the square
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is nnot an integer.
            ValueError: If value is less than or equal to 0
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the strng representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width
        )