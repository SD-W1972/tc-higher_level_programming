#!/usr/bin/python3
"""
Square class module
This module defines a Square class with private size attribute
"""


class Square:
    """
    A class that defines a square with private size attribute

    Attributes:
        __size (int): Private instance attribute representing
                     the size of the square's side

    Args:
        size (int): The size of the square

    Note:
        The size attribute is kept private to allow the class
        to control and validate its value in future implementations
    """

    def __init__(self, size):
        """
        Initializes a new Square instance

        Args:
            size (int): The size of the square's side
        """
        self.__size = size
