#!/usr/bin/python3
"""Module that defines a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using its JSON representation.

    Args:
        my_obj: the object to serialize and save.
        filename: the path to the file to write.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
