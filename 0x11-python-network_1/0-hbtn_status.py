#!/usr/bin/python3
""" Fetch response from URL using urllib package """

from urllib import request


if __name__ == "__main__":
    """ Make a request to https://intranet.hbtn.io/status """
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf8")))
