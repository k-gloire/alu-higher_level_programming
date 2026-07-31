#!/usr/bin/python3
"""Module that defines a function to print a square of hashes.

This module provides print_square, which prints a square made of the
character # with a given side length.
"""


def print_square(size):
    """Print a square of # characters with the given side length.

    Args:
        size: the length of each side of the square, a non-negative
            integer.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
