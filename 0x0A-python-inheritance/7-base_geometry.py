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
