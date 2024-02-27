#!/usr/bin/python3

import json

"""initialize a class"""


class Base:
    """A new class created."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a base object.

        Args:
            id(int): that is the Id of the object
            if not provided, a new id will be assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: A JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
