#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantianting new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ('first_name',)

    def __init__(self):
        pass
