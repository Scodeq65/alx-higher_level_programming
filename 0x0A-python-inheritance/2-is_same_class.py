#!/usr/bin/python3
"""A function to check if an object is an instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        true if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
