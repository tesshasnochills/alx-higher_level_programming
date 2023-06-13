#!/usr/bin/python3


"""
a function that returns true is the object is exactly an
instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    return true if instance else return false
    """
    if type(obj) == a_class:
        return True
    return False
