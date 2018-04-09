#!/usr/bin/python3
""" Send request to URL & dispaly value of X-Request-Id from response """

from urllib import request
from sys import argv


if __name__ == "__main__":
    """ Send request to URL argument and display parsed results """
    with request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))

# Ref: https://stackoverflow.com/questions/14949644/
# python-get-header-information-from-url
