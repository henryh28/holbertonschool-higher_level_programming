#!/usr/bin/python3
"""
Module content
10-square - Create Square class that extends Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Create a Square class that extends Rectangle class """
    def __init__(self, size):
        """ Initialization constructor method """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
