#!/bin/bash
# Takes in URL and displays all HTTP methods that the server will accept
curl -si -X OPTIONS "$1" | grep "Allow" | cut -c 8-
