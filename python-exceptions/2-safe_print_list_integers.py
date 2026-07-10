#!/usr/bin/python3
"""Module for printing only the integers in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers in my_list, skipping other types.

    Returns the number of integers printed. If x is larger than the
    list, an IndexError is allowed to propagate.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
