#!/usr/bin/python3


def best_score(my_dict):
    return (None if not my_dict else sorted(my_dict, key=my_dict.get)[-1])
