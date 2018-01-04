#!/usr/bin/python3


class Square:
    """ This class defines a square object """

    def __init__(self, size=0, position=(0, 0)):
        """ Constructor for the Square class """
        self.__size = size
        self.__position = position

    def area(self):
        """ Returns area of the object """
        return self.__size * self.__size

    def my_print(self):
        """ Output object using '#' character """
        if (self.__size == 0):
            print()
            return

        print("\n" * self.__position[1], end="")

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
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

    @property
    def position(self):
        """ Getter for object's 'position' attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for object's 'position' attribute """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
