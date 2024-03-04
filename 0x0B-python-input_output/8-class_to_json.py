#!/usr/bin/python3
"""A function that returns dictionary."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj: An instance of a class
    Return:
        dict: The dictionaryy description of the object.
    """
    return obj.__dict__
