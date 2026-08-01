#!/usr/bin/python3
"""Module that defines the Square class.

This module provides the Square class, which inherits from Rectangle
and represents a square as a special case of a rectangle where width
and height are always equal.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, inheriting behavior from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size: the length of each side of the square, a positive
                integer.
            x: the horizontal offset of the square, an integer
                greater than or equal to 0. Defaults to 0.
            y: the vertical offset of the square, an integer greater
                than or equal to 0. Defaults to 0.
            id: the id to assign to this instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size (side length) of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, updating width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyworded arguments.

        Args:
            args: new attribute values in the order id, size, x, y.
                Used only if non-empty.
            kwargs: new attribute values by name. Ignored if args is
                non-empty.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of this Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
