#!/bin/bash
# Take in URL, send request to that URL & display size of response body
curl -sI "$1" | grep "Content-Length" | cut -d ":" -f2
