#!/usr/bin/python3
"""
Module Content
2-is_same_class - Return True/False depending on if object is exactly an
                  instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, False if not
    """
    return (type(obj) == a_class)
