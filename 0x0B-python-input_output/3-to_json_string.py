#!/usr/bin/python3
"""A JSON representation of object."""

import json


def to_json_string(my_obj):
    """Return the JSON rep of an object (string).
    Args:
        My_obj: The object to be serialized to JSON.
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
