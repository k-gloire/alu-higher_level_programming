#!/usr/bin/python3
"""My class module."""


class MyClass:
    """My class."""

    def __init__(self, name):
        """Initialize a new MyClass instance.

        Args:
            name: the name for this instance.
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """Return the string representation of this instance."""
        return "[MyClass] {} - {:d}".format(self.name, self.number)
