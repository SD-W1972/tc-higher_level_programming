#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle with width and height"""

    def __init__(self, width, height):
        """Initialize rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return rectangle area"""
        return self.__height * self.__width

    def __str__(self):
        """Return string representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
