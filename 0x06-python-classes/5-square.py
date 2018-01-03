#!/usr/bin/python3


class Square:
    """ This class defines a square object """

    def __init__(self, size=0):
        """ Constructor for the Square class """
        self.__size = size

    def area(self):
        """ Returns area of the object """
        return self.__size * self.__size

    def my_print(self):
        """ Output object using '#' character """
        if (self.__size == 0):
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

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
