#!/usr/bin/python3
"""Module that defines a function to convert an object to a JSON-ready dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dictionary, string, integer, boolean).

    Returns:
        A dictionary representation of obj's attributes.
    """
    return obj.__dict__
