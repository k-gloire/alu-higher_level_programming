#!/usr/bin/python3
"""Module for safely printing x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of my_list, return the number actually printed."""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
