#!/usr/bin/python3

"""Defines a function that returns the list of available attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

        Returns:
            A listt of available attributes and methods of the object.
    """
    return dir(obj)
