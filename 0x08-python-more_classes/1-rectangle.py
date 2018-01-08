#!/usr/bin/python3
"""
Create a class that defines a rectangle
"""


class Rectangle:
    """ This class defines a Rectangle object """

    def __init__(self, width=0, height=0):
        """ Constructor for the Rectangle class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for 'width' attribute """
        return self.__width

    @property
    def height(self):
        """ Getter for 'height' attribute """
        return self.__height

    @width.setter
    def width(self, width):
        """ Setter for 'width' attribute """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ Setter for 'height' attribute """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
