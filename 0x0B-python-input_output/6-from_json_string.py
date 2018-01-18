#!/usr/bin/python3
"""
Module content
6-from_json_string.py   - Return a Python data structure object
                          represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ Return a python data structure represented by a JSON string """
    return json.loads(my_str)
