#!/usr/bin/python3
"""Module that defines the Rectangle class.

This module provides the Rectangle class, which inherits from Base
and represents a rectangle defined by width, height, and position.
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle, inheriting id management from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width: the width of the rectangle, a positive integer.
            height: the height of the rectangle, a positive integer.
            x: the horizontal offset of the rectangle, an integer
                greater than or equal to 0. Defaults to 0.
            y: the vertical offset of the rectangle, an integer
                greater than or equal to 0. Defaults to 0.
            id: the id to assign to this instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, validating the new value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, validating the new value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal offset, validating the new value."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical offset, validating the new value."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the # character, respecting x/y."""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyworded arguments.

        Args:
            args: new attribute values in the order id, width,
                height, x, y. Used only if non-empty.
            kwargs: new attribute values by name. Ignored if args is
                non-empty.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of this Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
