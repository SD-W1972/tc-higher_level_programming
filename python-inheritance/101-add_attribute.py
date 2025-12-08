#!/usr/bin/python3
"""Add attribute to object if possible"""


def add_attribute(obj, name, value):
    """Add attribute to object or raise TypeError"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
