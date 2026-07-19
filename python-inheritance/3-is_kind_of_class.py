#!/usr/bin/python3
"""Module that defines a function to check class membership by inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or one of its subclasses.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a_class or a class that inherits
        from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
