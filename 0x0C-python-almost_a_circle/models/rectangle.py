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

    def to_dictionary(self):
        """Retuens the dictionary representation of the rectangle.
        Returns:
            dict: A dictionary containing the attributes of the
            rectangle.
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle representated by '#' character."""
        print("\n" * self.y, end="")
        for _ in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle instance based on the
        provided arguments.

        Args:
            *args: The arguments to assign to the attributes in the order
            (id, width, lenght, height, x, y)
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the Rectangle instance.
        Returns:
            str: A string rep of the rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(
                self.id, self.x, self.y, self.width, self.height
        )
