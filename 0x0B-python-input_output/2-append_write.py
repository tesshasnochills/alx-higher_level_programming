#!/usr/bin/python3
"""module: write function"""


def append_write(filename="", text=""):
    """write file- a function that writes text ina file

    Args:
        @filename: name of the file
        @text: text to be written in the file
    """

    count = 0
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
