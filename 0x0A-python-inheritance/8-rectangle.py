#!/usr/bin/python3
"""
Module content
8-rectangle - Create Rectangle class that extends BaseGeometry class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class extends BaseGeometry class
    """

    def __init__(self, width, height):
        """ Initialization constructor method """
        self.integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
