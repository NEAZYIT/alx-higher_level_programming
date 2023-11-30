#!/bin/bash
# Sends a JSON POST request to a specified URL using content from a file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
