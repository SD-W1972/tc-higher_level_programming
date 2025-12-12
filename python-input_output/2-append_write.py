#!/usr/bin/python3
"""Append write module"""


def append_write(filename="", text=""):
    """
    append_write function

    Args:
        filename (string)
        text (string)

    Returns:
        the number of characters added
    """
    with open(filename, "a") as file:
        file.append(text)
    return len(text)
