#!/usr/bin/python3
"""Module that defines a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from the JSON content of a file.

    Args:
        filename: the path to the JSON file to read.

    Returns:
        The Python data structure represented by the file's content.
    """
    with open(filename, "r") as f:
        return json.load(f)
