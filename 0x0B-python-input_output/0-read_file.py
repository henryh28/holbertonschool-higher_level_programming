#!/usr/bin/python3
"""
Module content

0-read_file   - Contains function to read UTF8 text files and print to stdout
"""


def read_file(filename=""):
    """ Read UTF8 text files and print content to stdout """
    with open(filename, "r", encoding="utf-8") as f:
            print(f.read(), end="")
