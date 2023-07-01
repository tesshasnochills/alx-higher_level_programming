#!/usr/bin/python3
""" module: student class"""


class Student():
    """public variables"""
    first_name = None
    last_name = None
    age = 0

    """init function"""
    def __init__(self, first_name, last_name, age):
        """
        Args:
            @first_name: the first name
            @last_name: the last name
            @age: the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ public method to json that retrieves the dic rep of a student"""
    def to_json(self):
        """to json - retrieve dict rep of a student"""
        return self.__dict__
