#!/usr/bin/python3
"""Module for deleting a key from a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete a key from a_dictionary if it exists."""
    a_dictionary.pop(key, None)
    return a_dictionary
