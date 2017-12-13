#!/bin/usr/python3


def add_tuple(tuple_a=(), tuple_b=()):

    length = min(len(tuple_a), len(tuple_b))

    if (length == 2):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif (length == 1):
        second = tuple_a[1] if len(tuple_a) > len(tuple_b) else tuple_b[1]
        return (tuple_a[0] + tuple_b[0], second)
    elif (length == 0):
        if (len(tuple_a) > len(tuple_b)):
            return (tuple_a[0], tuple_a[1])
        else:
            return (tuple_b[0], tuple_b[1])
