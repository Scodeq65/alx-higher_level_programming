#!/usr/bin/python3
"""A function that returns True is the obj is an instance of a class
    that inherited from the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """Check if the object inherits (directly or indirectly) from
        a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj inherits (directly or indirectly) froam a_class,
        False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
