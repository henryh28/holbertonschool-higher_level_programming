#!/usr/bin/python3
"""
Module content
0-lookup - Returns list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns list of available attributes and methods of an object
    """
    return (dir(obj))
