#!/usr/bin/python3
"""
Module Content
4-inherits_from - Returns True/False depending on if object is derived
                  from a specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is derived from a_class, False if not
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
