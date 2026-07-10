#!/usr/bin/python3
"""Module for finding elements present in only one set."""


def only_diff_elements(set_1, set_2):
    """Return a set of elements present in only one of the two sets."""
    return set_1 ^ set_2
