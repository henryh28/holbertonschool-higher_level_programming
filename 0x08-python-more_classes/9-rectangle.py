#!/usr/bin/python3
"""
Create a class that defines a rectangle
"""


class Rectangle:
    """ This class defines a Rectangle object """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor for the Rectangle class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Return area of current rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return perimeter of current rectangle """
        return (0 if (self.__width is 0 or self.__height is 0) else (
            self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Overwrites __str__ magic method """
        return ("" if (self.__width is 0 or self.__height is 0) else (
            "\n".join(["{}".format(self.print_symbol) * self.__width for
                       row in range(self.__height)])))

    def __repr__(self):
        """ Overwites __repr__ magic method """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Destructor method """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger rectangle based on its area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return (rect_1 if (rect_1.area() >= rect_2.area()) else rect_2)

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle object """
        return (cls(size, size))
