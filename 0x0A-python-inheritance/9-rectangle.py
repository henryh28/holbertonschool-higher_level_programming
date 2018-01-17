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

    def area(self):
        """ Return area of current Rectangle object """
        return (self.__width * self.__height)

    def __str__(self):
        """ Returns string description of current object """
        return ("[{}] {}/{}".format(__class__.__name__, self.__width,
                                    self.__height))
