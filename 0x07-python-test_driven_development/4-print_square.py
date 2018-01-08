#!/usr/bin/python3
"""
Print out a grid of user selected size using '#'
"""


def print_square(size):
    """
    Print out a grid with height and width of 'size' using '#'
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for element in range(size):
            print("#", end="")
        print()
