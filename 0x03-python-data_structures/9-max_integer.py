#!/usr/bin/python3


def max_integer(my_list=[]):
    return (None if len(my_list) < 1 else sorted(my_list)[-1])
