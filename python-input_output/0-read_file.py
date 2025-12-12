#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    Read file and print its content

    Args:
        filename (str): Path to the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
