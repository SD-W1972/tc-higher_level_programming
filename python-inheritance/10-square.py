#!/usr/bin/python3
"""Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square with size"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return square area"""
        return self.__size * self.__size
