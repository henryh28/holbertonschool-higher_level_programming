#!/usr/bin/python3
""" Use the 'requests' package to make a request to specified URL """

from requests import get


if __name__ == "__main__":
    """ Use 'requests' package to make a request to holberton intranet """

    response = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
