#!/usr/bin/python3
"""initialize a class"""


class Base:
    """A new class created."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializez a base object.

        Args:
            id(int): that is the Id of the object
            if not provided, a new id will be assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
