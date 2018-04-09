#!/usr/bin/python3
""" Send request to URL and display body of response decoded in utf-8 """

from requests import get
from sys import argv


if __name__ == "__main__":
    """ Display result of URL request decoded in utf-8 """

    response = get(argv[1])
    status = response.status_code

    print("Error code: {}".format(status) if status >= 400 else response.text)
