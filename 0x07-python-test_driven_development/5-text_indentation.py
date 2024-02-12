#!/usr/bin/python3
"""
A function that prints a square with the character #
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each occurrence of '.', '?' and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    line = ''
    for char in text:
        if char in punctuations:
            lines.append(line.strip())
            lines.append(['', ''])
            line = ''
        else:
            line += char
    lines.append(line.strip())

    for line in lines:
        print(*lines, sep='\n')
