#!/usr/bin/python3
"""Module that defines a function to check strict inheritance."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a class that inherited (directly
        or indirectly) from a_class, but obj's own class is not a_class
        itself, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
