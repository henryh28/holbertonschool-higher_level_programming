#!/usr/bin/python3
"""
Outputs text argument verbatim, with the exception of adding
a newline if it encounters a '.', '?', or ':'
"""


def text_indentation(text):
    """
    Outputs text argument verbatim, with the exception of adding
    a newline if it encounters a '.', '?', or ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in text:
        print (character, end="")
        if character in ".?:":
            print("\n")
