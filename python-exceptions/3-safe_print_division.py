#!/usr/bin/python3
"""Module for safely dividing two integers."""


def safe_print_division(a, b):
    """Divide a by b, printing the result in a finally block."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
