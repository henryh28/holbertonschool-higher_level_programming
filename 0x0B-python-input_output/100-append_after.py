#!/usr/bin/python3
"""
Module content
100-append_after   - Insert a line of text to a file, after each line
                     containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Insert new_string in lines containing search_string """
    image = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            image += line + new_string if search_string in line else line

    with open(filename, "w", encoding="utf-8") as f:
        f.write(image)
