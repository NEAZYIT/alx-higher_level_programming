#!/bin/bash
# Sends a GET request with a custom header to a URL and displays the body of the response
curl -sH "X-School-User-Id: 98" -X GET "$1"
