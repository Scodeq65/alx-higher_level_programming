#!/usr/bin/python3
"""
A function that print a formated string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the anme with thye given first name and last name.

    Args:;
        first_name (str): the first anem
        last_name (str, optional): The last name. Defaults to an empty str "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
