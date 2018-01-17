#!/usr/bin/python3
"""
Module content
1-my_list - Prints a sorted list in ascending order
"""


class MyList(list):
    """
    Extends list
    """

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        """
        print(sorted(self))
