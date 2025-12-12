#!/usr/bin/python3
"""Create object from a JSON file module"""
import json


def load_from_json_file(filename):
    """Load object from JSON file (creates but doesn't return)"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
