#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """
    write_file function

    Args:
        filename (string)
        text (string)

    Returns the number of characters wrote
    """
    with open(filename, 'w') as file:
        file.write(text)

    return len(text)
