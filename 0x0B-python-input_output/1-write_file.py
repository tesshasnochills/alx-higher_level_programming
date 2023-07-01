#!/usr/bin/python3
""" module: write function """


def write_file(filename="", text=""):
    """ write file- function that writes text in a file

    Args:
        @filename: name of the file
        @text: text to be written in file
    """

    with open(filename, 'w', encoding="utf-8") as myFile:
        myFile.write(text)
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        return len(read)
