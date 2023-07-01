#!/usr/bin/python3


"""
module: is kind of a class function used to
check if is instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    return true of isisnstance else return false
    """
    if isinstance(obj, a_class):
        return True
    return False
