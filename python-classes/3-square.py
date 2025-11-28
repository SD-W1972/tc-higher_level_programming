#!/usr/bin/python3
"""
Square class module
This module defines a Square class with
size validation and area calculation
"""


class Square:
    """
    A class that defines a square with
    private size attribute and area method

    Attributes:
        __size (int): Private instance attribute representing
                     the size of the square's side

    Args:
        size (int, optional): The size of the square.
        Defaults to 0.

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance
        with size validation

        Args:
            size (int, optional): The size of the
            square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size
