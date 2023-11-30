#!/bin/bash
# Displays all HTTP methods accepted by a server for a specified URL
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
