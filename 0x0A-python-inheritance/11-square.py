#!/usr/bin/python3
"""
Module content
11-square - Create Square class that extends Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Create a Square class that extends Rectangle class """
    def __init__(self, size):
        """ Initialization constructor method """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Returns string description of current object """
        return ("[{}] {}/{}".format(__class__.__name__, self.__size,
                                    self.__size))
