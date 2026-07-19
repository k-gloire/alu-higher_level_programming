#!/usr/bin/python3
"""Module that defines a function to list attributes/methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.

    Returns:
        A list containing all attributes and methods of obj.
    """
    return dir(obj)
