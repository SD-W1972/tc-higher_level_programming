#!/usr/bin/python3
"""Class to JSON serialization module"""


def class_to_json(obj):
    """
    Return dictionary description for JSON serialization of an object

    Args:
        obj: Instance of a class with serializable attributes

    Returns:
        dict: Dictionary with object's attributes
    """
    return obj.__dict__
