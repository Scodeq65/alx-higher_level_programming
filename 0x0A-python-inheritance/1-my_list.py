#!/usr/bin/python3

"""This module provides a class Mylist that extends the built-in class
    with additional functionality.
"""


class MyList(list):
    """a subclass of list that provides additional funcionality."""

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""

        sorted_list = sorted(self)
        print(sorted_list)
