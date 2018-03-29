#!/bin/bash
# Send a GET request to URL and display the status code of resposne
curl -s -o /dev/null -w "%{http_code}" "$1"
