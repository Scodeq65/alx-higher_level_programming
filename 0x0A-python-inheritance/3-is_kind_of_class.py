#!/usr/bin/python3
"""Define a function that returns True if the object is an instance of, 
    or if the object is an instance of a class that inherited from,
    otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of, or inherited from, a_class, Fals otherwise
    """
    return isinstance(obj, a_class)
