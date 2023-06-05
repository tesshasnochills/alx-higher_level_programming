#!/usr/bin/python3
""" creating rectangle class """


class Rectangle:
    """ initialising the rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """ setting the rectangle variables

        Args:
            width (int): width of rectangle
            height (int): height if rectangle
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Function that returns the perimeter of the rectangle,
        if the height and wdth are not equal to zero
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ A function to return the printable representation
        of the rectangle in question
        represents it with # """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """ return the string representation of the rectangle """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ prints a message when a rectangle is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
