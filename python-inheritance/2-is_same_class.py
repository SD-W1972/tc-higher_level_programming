#!/usr/bin/python3
"""
Is same class module
This module provides a function to see if a provided
object is an instance from a provided class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance from a_class,
    returns False if it's not"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
