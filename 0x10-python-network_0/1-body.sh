#!/bin/bash
# Sends a GET request to a URL and displays the body of the response for a 200 status code
curl -sLw "\n%{http_code}" -X GET "$1" -o /tmp/body_file | tail -n 1 | grep -q '^200$' && cat /tmp/body_file
