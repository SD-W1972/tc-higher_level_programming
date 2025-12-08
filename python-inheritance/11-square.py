#!/usr/bin/python3
"""Square module inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square with size"""

    def __init__(self, size):
        """Instantiates the square object with size"""
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """Returns the square area"""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of square"""
        return "[Square {}/{}]".format(self.__size, self.__size)
