#!/usr/bin/python3
"""Writes an Object to a text file."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON rep.
    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write to.
    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
