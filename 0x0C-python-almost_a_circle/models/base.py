#!/usr/usr/bin/python3
"""module for the base model"""
import json
import os.path
import csv


class Base:
    """initializing the number of the object variables"""
    __nb_objects = 0

    def __init__(self, id=None):
        """creating the init function

        Args:
            @id: the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
