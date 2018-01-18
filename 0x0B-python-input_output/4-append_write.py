#!/usr/bin/python3
"""
Module content
4-append_write   - Append a string to a text file using UTF8 encoding and
                   return number of characters added
"""


def append_write(filename="", text=""):
    """ Return number of characters appended to a text file """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
