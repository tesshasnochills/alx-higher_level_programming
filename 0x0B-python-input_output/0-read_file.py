#!/usr/bin/python3
"""
Readfile function
"""


def read_file(filename=""):
    """ readfile - function that reads a file

    Args:
        @filename = name of the file
    """

    with open(filename, encoding="utf-8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")
