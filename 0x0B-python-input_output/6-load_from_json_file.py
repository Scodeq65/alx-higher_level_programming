#!/usr/bin/python3
"""Create an Object from a JSON file."""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file.
    Args:
        filename (str): The name of the JSON file to laod from.
    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
