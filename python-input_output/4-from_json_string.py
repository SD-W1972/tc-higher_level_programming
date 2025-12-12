#!/usr/bin/python3
"""Json string to object module"""

import json


def from_json_string(my_str):
    """
    from_json_string function

    Args:
        my_str (string)

    Returns:
        Json obj
    """
    return json.loads(my_str)
