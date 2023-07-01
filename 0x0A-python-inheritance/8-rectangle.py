#!/usr/bin/python3
"""
a class BaseGeometry
"""


class BaseGeometry:
    """ a public instance method area"""
    def area(self):
        raise Exception("area() is not implemented")

    """integer validator"""
    def integer_validator(self, name, value):
        """integer validator

        Args:
            name (string): a sting
            value(int): integer value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    implements a rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
