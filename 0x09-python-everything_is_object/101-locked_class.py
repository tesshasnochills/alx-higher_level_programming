#!/usr/bin/python3

"""
Class methods that prevent dynamically creating attributes

"""


class LockedClass:
    """prevent dynamic allocation"""
    __slots__ = ['first_name']

    def __init__(self):
        """ init without attributes """
        pass
