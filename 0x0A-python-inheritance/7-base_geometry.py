#!/usr/bin/python3
"""
Module content
7-base_geometry - Implements a BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """ Returns area of object """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
