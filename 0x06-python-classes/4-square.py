#!/usr/bin/python3


class Square:
    """ This class defines a square object """

    def __init__(self, size=0):
        """ Constructor for the Square class """
        self.__size = size

    def area(self):
        """ Returns area of the object """
        return self.__size * self.__size

    @property
    def size(self):
        """ Getter for object's 'size' attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for object's 'size' attribute """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
