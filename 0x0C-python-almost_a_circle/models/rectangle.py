#!/usr/bin/python3
"""This module defines the rectangle class, which inherites from
the Base class.
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class inheriting from a Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilizes a Rectangle object.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle position.
            y (int): the y-coordinate of the rectangle position.
            id (int): The Id of the rectangle, If not provided,
            a new one will be craeted
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The value to set as the width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """Getting the method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute.
        Args:
            value: (int): The value to set as the height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """Getting method for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x attribute.

        Args:
            value (int): The value to be set as the x-cordiante of the
            retangle's position
        """
        self.__x = value

    @property
    def y(self):
        """Getter mothod for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y attribute.
        Args:
            value (int): The value to be set as the y-coordinate of the
            rectangle's position.
        """
        self.__y = value
