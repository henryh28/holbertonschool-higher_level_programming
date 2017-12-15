#!/usr/bin/python3


def best_score(my_dict):
    return (None if my_dict is None else sorted(my_dict, key=my_dict.get)[-1])

#dictionaries are ordered in python 3.6+, no need to sort then
