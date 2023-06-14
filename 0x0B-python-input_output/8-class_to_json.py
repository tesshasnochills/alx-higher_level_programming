#!/usr/bin/python3
"""module: class to json """


def class_to_json(obj):
    """class_to_json - converts a class obj to json

    Args:
        @obj: the class being converted
    """
    return obj.__dict__
