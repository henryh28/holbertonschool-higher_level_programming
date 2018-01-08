#!/usr/bin/python3
"""
Adds 2 integers together.  a and b must be integers or floats,
otherwise raise a TypeError exception.

Convert a and/or b to integers first if they are floating point values

Returns: Result of a + b
"""


def add_integer(a, b):
    """
    Add a to b if both are ints or floats. Else raise a TypeError
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return (int(a) + int(b))

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
