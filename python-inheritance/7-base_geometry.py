#!/usr/bin/python3
"""
Base geometry module
This class provides a non implemented area
method
"""


class BaseGeometry:
    """
    Base Geometry class
    """
    def area(self):
        """
        Area method

        Raises an Exception
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """This method validates the value attribute"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
