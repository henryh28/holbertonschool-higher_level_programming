#!/usr/bin/python3
"""
Module content
2-read_lines.py   - Print 'x' lines of UTF8 text file to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    Print nb_lines number of lines to stdout. Unless nb_lines is 0 or
    is greater than the total number of lines in file, in which case
    print out entire content of file
    """
    line_count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
            line_count += 1

            if line_count >= nb_lines and nb_lines > 0:
                break
