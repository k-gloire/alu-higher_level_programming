#!/usr/bin/python3
"""Module that defines a Square class with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, defined by a private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of each side of the square.
        """
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
