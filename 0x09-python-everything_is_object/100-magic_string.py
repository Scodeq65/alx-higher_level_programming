#!/usr/bin/python3
"""Initialize a magic_string."""


def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Bestschool, " * (magic_string.n - 1) + "Bestschool")
