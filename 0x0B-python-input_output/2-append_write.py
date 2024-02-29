#!/usr/bin/python3
"""Appends astring to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8) and
    return the number of characters added.
    Args:
        filename (str): The name of the file to append to
        (default is empty file)
        text (str): The string to append to the file
        (efault is empty string)
    Returns:
        int: The num of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_of_char_added = file.write(text)

    return num_of_char_added
