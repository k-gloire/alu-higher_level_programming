#!/usr/bin/python3
"""Module for safely printing a value as an integer."""


def safe_print_integer(value):
    """Print value as an integer. Return True on success, False otherwise."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
