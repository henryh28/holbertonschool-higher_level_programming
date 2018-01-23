#!/usr/bin/python3
"""
Module content
square   - Extends the 'Base->Rectangle' class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class 'Square' extends class 'Rectangle' """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization constructor method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for 'size' attribute """
        return (self.width)

    @size.setter
    def size(self, size):
        """ Setter for 'size' attribute """
        self.validate("width", size, 0)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates current object's attributes """
        attr_list = ["id", "size", "x", "y"]

        if (args):
            for i in range(len(args)):
                if (attr_list[i] == "size"):
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attr_list[i], args[i])
        elif(kwargs):
            for key, value in kwargs.items():
                if (key == "size"):
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of current object """
        return({"id": self.id, "size": self.size, "x": self.x,
                "y": self.y})

    def __str__(self):
        """ Returns user facing string representation of object """
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width))
