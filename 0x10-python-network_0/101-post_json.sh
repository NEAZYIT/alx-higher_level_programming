#!/bin/bash
# Sends a JSON POST request to a specified URL using content from a file
[ -z "$2" ] && echo "Usage: $0 <URL> <JSON_FILE>" && exit 1
jq . "$2" &> /dev/null || { echo "Not a valid JSON"; exit 1; }
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
