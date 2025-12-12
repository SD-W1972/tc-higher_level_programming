#!/usr/bin/python3
"""Create object from a JSON file module"""
import json


def load_from_json_file(filename):
    """
    Load object from JSON file

    Args:
        filename (str): Name of JSON file

    Returns:
        object: Python object loaded from JSON
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
