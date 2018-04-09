#!/usr/bin/python3
""" Send a string as a param to the star wars API """

from requests import get
from sys import argv


if __name__ == "__main__":
    """ Send a string as a param to the Star Wars API """

    response = get("http://swapi.co/api/people/?search={}".format(argv[1]))
    json = response.json()
    print("Number of results: {}".format(json["count"]))

    for result in json["results"]:
        print(result["name"])
