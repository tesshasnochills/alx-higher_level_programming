#!/usr/bin/python3
""" module: to json string"""
import json


def to_json_string(myobj):
    """ to_json_string- rturns the JSON representation of
    an object string

    Args:
        @myobj: object string to convert to json
    """
    return json.dumps(myobj)
