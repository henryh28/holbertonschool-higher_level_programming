#!/usr/bin/python3


def best_score(my_dict):
    return (None if my_dict is None else sorted(my_dict, key=my_dict.get)[-1])
