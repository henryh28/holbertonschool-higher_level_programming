#!/usr/bin/python3
"""
Module content
3-write_file   - Write a string to a text file using UTF8 encoding and
                 return number of characters written
"""


def write_file(filename="", text=""):
    """ Return number of characters written to a text file """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
