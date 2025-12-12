#!/usr/bin/python3
"""Save object to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to file as JSON"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
