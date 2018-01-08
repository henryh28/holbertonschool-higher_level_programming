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
    leading = True
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in text:
        if character is " " and text is not " ":
            if leading is False:
                print(character, end="")
        else:
            print(character, end="")
            leading = False

        if character in ".?:":
            leading = True
            print("\n")
