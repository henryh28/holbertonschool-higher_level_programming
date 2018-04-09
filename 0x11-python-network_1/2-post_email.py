#!/usr/bin/python3
""" Send POST request to URL with email address as URL paramter """

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    """ Display response body of POST request to URL with email param """

    data = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], data=data)
    response = request.urlopen(req).read()
    print(response.decode("utf8"))

# Ref: https://stackoverflow.com/questions/48841889/
# how-do-i-add-a-parameter-to-a-post-requests-body-with-urllib
