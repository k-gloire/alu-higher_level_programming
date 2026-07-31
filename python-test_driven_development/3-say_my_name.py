#!/usr/bin/python3
"""Module that defines a function to print a formatted name.

This module provides say_my_name, which prints a person's first and
last name in the format "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """Print a person's name in the format "My name is <first> <last>".

    Args:
        first_name: the person's first name, a string.
        last_name: the person's last name, a string. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
