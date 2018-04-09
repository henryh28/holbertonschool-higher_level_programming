#!/usr/bin/python3
""" Submit credentials to github API and display associated account id """


from requests import get
from sys import argv


if __name__ == "__main__":
    """ Submit credentials to githubh API and display associated id """

    response = get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(response.json()["id"] if "id" in response.json() else "None")

# Ref: https://github.com/requests/requests
