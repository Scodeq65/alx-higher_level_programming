#!/usr/bin/python3
"""A function that writes a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UFT8) and return
    a number of character.

    Args:
        filename (str): The name of the filr to write to
        (default is empty file)
        text (str): The string to write to the file
        (default is empty string)
        
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)

    return num_chars_written
