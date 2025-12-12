#!/usr/bin/python3
""" String to json module """

import json


def to_json_string(my_obj):
    """
    to_json_string function

    Args:
        my_obj (string)

    Returns:
        json object of my_obj
    """
    return json.dumps(my_obj)
