#!/bin/bash
# Reference: https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
curl -X POST -sH "Content-Type: application/json" -d "@$2" "$1"
