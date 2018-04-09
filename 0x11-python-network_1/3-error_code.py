#!/usr/bin/python3
""" Send request to URL and display body of response decoded in utf-8 """

from urllib import request
from urllib import error
from sys import argv


if __name__ == "__main__":
    """ Display result of URL request decoded in utf-8 """
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf8"))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
