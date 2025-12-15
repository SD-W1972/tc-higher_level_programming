#!/usr/bin/python3
"""Student class module"""


class Student:
    """Represents a student with personal information"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of student for JSON"""
        return self.__dict__
