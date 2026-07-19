#!/usr/bin/python3
"""Module that defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, defined by a private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of each side of the square.
        """
        super().__init__(size, size)
