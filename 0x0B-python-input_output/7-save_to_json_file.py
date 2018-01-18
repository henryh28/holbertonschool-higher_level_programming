#!/usr/bin/python3
"""
Module content
7-save_to_json_file   - Write an object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ Write my_obj to 'filename' using JSON """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
