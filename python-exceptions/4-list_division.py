#!/usr/bin/python3
"""Module for dividing two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Return a new list of element-wise divisions of two lists."""
    new_list = []
    for i in range(list_length):
        divided = 0
        try:
            divided = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(divided)
    return new_list
