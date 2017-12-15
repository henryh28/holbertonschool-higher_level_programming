#!/usr/bin/python3


def complex_delete(my_dict, value):
    targets = [k for k, v in my_dict.items() if v == value]
    for boom in targets:
        del my_dict[boom]

    return (my_dict)
