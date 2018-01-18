#!/usr/bin/python3
"""
Module content
1-number_of_lines   - Return number of lines in a text file
"""


def number_of_lines(filename=""):
    line_number = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line_number += 1

    return (line_number)
