#!/usr/bin/python3
"""
Module content
10-class_to_json.py   - Return dictionary description with simple data
                        structure for JSON serialized object
"""


def class_to_json(obj):
    """ Return dictionary description for JSON serialization of object """

    return (obj.__dict__)
