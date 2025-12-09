#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of shape"""
        pass


class Circle(Shape):
    """Circle shape implementation"""

    def __init__(self, radius):
        """Initialize circle with radius (uses absolute value)"""
        self.__radius = abs(radius)

    def area(self):
        """Calculate circle area"""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate circle perimeter (circumference)"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle shape implementation"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate rectangle perimeter"""
        return 2 * (self.__height + self.__width)


def shape_info(obj):
    """Print shape area and perimeter using duck typing"""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
