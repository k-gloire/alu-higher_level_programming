#!/usr/bin/python3
"""Module that defines a function to print indented text.

This module provides text_indentation, which prints a block of text
with two newlines inserted after each period, question mark, or
colon.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: the string to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    marks = ".?:"
    line = ""
    i = 0
    length = len(text)
    while i < length:
        char = text[i]
        if char == " " and line == "":
            i += 1
            continue
        line += char
        if char in marks:
            print(line.strip())
            print()
            line = ""
        i += 1
    if line.strip():
        print(line.strip(), end="")
