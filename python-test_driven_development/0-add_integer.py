#!/usr/bin/python3
"""
Add Integer Module
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first number (integer or float)
        b: second number (integer or float), default 98

    Returns:
        int: sum of a and b as integer
        
    Raises:
        TypeError: if a or b is not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
