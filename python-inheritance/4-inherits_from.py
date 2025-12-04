#!/usr/bin/python3
"""
Inherits from module
This module provides a function that checks
if a obj is an instance of a class that inherits
the provided class, but is not an instance of the class
itself
"""


def inherits_from(obj, a_class):
    """Returns True if the condition passes, False if it
    doesn't"""
    return isinstance(obj, a_class) and type(obj) is not a_class
