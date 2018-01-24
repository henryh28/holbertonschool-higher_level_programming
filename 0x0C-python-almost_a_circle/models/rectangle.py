#!/usr/bin/python3
"""
Module content
rectangle   - Create a Rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from 'Base' """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for 'width' attribute """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for 'width' attribute """
        self.validate("width", width, 0)
        self.__width = width

    @property
    def height(self):
        """ Getter for 'height' attribute """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for 'height' attribute """
        self.validate("height", height, 0)
        self.__height = height

    @property
    def x(self):
        """ Getter for 'x' attribute """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter for 'x' attribute """
        self.validate("x", x, -1)
        self.__x = x

    @property
    def y(self):
        """ Getter for 'y' attribute """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter for 'y' attribute """
        self.validate("y", y, -1)
        self.__y = y

    def area(self):
        """ Returns area of current rectangle """
        return (self.width * self.height)

    def display(self):
        """ Displays current object """
        print("\n" * self.y, end="")
        print("\n".join("{}".format(self.x * " ") + "#" * self.width
                        for row in range(self.height)))

    def __str__(self):
        """ Returns user facing string representation of object """
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height))

    def update(self, *args, **kwargs):
        """ Updates current object's attributes """
        attr_list = ["id", "width", "height", "x", "y"]

        if (args):
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        elif (kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of current object """
        return({"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y})

    @staticmethod
    def validate(name, value, floor):
        """ Validates attribute values before updating them """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= floor):
            raise ValueError("{} must be >{} 0".format(name, "" if
                                                       floor == 0 else "="))
