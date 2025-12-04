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
        """
        print_sorted method. This method utilizes a
        bubble sort algorithm

        Args:
            self

        Returns:
            the list obj sorted in ascending order
        """
        for i in range(len(list) - 1):
            swapped = False
            for j in range(0, len(list) - i - 1):
                if list[j] > list[j + 1]:
                    list[j], 
                    list[j + 1] = list[j + 1], list[j]
                    swapped = True
            if not swapped:
                break

        return list
