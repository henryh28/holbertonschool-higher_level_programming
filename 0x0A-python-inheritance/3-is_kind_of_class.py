#!/usr/bin/python3
"""
Module Content
3-is_kind_of_class - Return True/False depending on if object is an
                     instance of a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class, False if not
    """
    return (isinstance(obj, a_class))
