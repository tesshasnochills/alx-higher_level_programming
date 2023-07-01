#!/usr/bin/python3
""" module: save to json file """
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file- function saves object to a text file

    Args:
        @my_obj: object being saved
        @filename: name of the file
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        json_data = json.dumps(my_obj)
        myFile.write(json_data)
