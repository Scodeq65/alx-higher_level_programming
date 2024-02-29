#!/usr/bin/python3
"""A JSON representation of object."""

import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.
    Args:
        My_str: The json srting representing the object.
    Returns:
        str: The Python data structure represented by the Json string.
    """
    return json.loads(my_str)
