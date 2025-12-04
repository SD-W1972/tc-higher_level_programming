#!/usr/bin/python3
"""
Lookup module
This module provides a function that returns the
list of available attributes and methods of an object
"""


def lookup(obj):
    """
    lookup method

    Args:
        obj: any object
    
    Returns: list with available attributes and
    methods from obj
    """
    return dir(obj)
