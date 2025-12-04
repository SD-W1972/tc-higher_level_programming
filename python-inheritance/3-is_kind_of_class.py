#!/usr/bin/python3
"""
Check if object is instance of class or inherited class
This module provides a function to check if an object
is an instance of, or inherits from, a specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if it's an instance, False if
    it's not"""
    return isinstance(obj, a_class)
