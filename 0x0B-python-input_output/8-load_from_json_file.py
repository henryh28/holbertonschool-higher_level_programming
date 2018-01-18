#!/usr/bin/python3
"""
Module content
8-load_from_json_file   - Create an object from a file containing JSON
"""
import json


def load_from_json_file(filename):
    """ Create an object from 'filename' which contains JSON """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
