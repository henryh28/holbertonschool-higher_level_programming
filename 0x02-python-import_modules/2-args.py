#!/usr/bin/python3
from sys import argv

if (__name__ == "__main__"):
    arg_num = len(argv) - 1

    print("{:d} argument{:s}{:s}".format(arg_num, "" if arg_num == 1 else
                                         "s", "." if arg_num < 1 else ":"))
    for counter, value in enumerate(argv[1:], 1):
        print("{:d}: {:s}".format(counter, value))
