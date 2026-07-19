#!/usr/bin/python3
"""Module that defines a list class with a sorted print method."""


class MyList(list):
    """A list class that adds the ability to print itself in sorted order."""

    def print_sorted(self):
        """Print all elements of the list in ascending sorted order."""
        print(sorted(self))
