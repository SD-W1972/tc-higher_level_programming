#!/usr/bin/python3
"""Student class with JSON filtering"""


class Student:
    """Student information class"""

    def __init__(self, first_name, last_name, age):
        """Create student with name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary of specified attributes or all if None"""
        if attrs is None:
            return self.__dict__

        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(sef, json):
        """Replace all attributes from JSON dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
