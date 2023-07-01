#!/usr/bin/python3


"""
function that returns True if object is instance of class that
inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    returns true if object is an instance of a class
    else false
    """
    return type(obj) != a_class and isinstance(obj, a_class)
