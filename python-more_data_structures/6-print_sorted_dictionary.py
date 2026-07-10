#!/usr/bin/python3
"""Module for printing a dictionary sorted by key."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary's key/value pairs sorted by key."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
