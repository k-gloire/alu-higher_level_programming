#!/usr/bin/python3
"""Module for finding the key with the highest value."""


def best_score(a_dictionary):
    """Return the key with the highest integer value."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
