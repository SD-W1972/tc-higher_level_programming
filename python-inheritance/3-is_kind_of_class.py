#!/usr/bin/python3
"""
Is kind of class module
This module provides a method tha verifies if
a provided obj is an istance of a provided class
or if, its an instance of a class that inherited
from the provided class
"""
def is_kind_of_class(obj, a_class):
    """Returns True if it's an instance, False if
    it's not"""
    return isinstance(obj, a_class)
