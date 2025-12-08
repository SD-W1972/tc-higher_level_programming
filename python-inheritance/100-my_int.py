#!/usr/bin/python3
"""MyInt class inheriting from int"""


class MyInt(int):
    """MyInt with inverted operators"""

    def __eq__(self, value):
        """Override == operator"""
        return not super().__eq__(value)

    def __ne__(self, value):
        """Override != operator"""
        return not super().__ne__(value)
