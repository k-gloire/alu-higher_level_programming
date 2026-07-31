#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides add_integer, which adds two numbers together
after casting any float arguments down to integers first.
"""


def add_integer(a, b=98):
    """Add two integers together, casting floats to int first.

    Args:
        a: the first number, an int or a float.
        b: the second number, an int or a float. Defaults to 98.

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
