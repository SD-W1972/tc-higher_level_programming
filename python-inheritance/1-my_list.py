#!/usr/bin/python3
"""
Sort a list module
This module provides a function that
sorts a list from ascending order 
"""


class MyList(list):
    """
    A class that defines a method to sort the inherited
    list

    Inherits:
        list
    """
    def print_sorted(self):
        """Prints list sorted without modifying original"""
        temp_list = self[:]

        n = len(temp_list)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if temp_list[j] > temp_list[j + 1]:
                    temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]

        print(temp_list)
