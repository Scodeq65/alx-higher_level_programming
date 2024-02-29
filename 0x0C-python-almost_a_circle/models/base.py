#!/usr/bin/python3
"""initialize a class"""

import json


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
    def to_json_string(list_objs):
        """Returns the JSON string representation of list_objs."""
        if list_objs is None or len(list_objs) == 0:
            return "[]"
        else:
            return json.dumps([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON str rep of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
