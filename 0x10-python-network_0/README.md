# 0x10. Python - Network #0 🌐

![Python - Network](https://github.com/NEAZYIT/alx-higher_level_programming/assets/121446147/70102d8e-1ba8-49ed-8564-c7ffe77baade)

## Description 📄
This repository contains solutions to tasks involving Bash scripting and Python programming related to network interactions and server requests. All scripts and solutions aim to adhere to specific requirements detailed below.

## Requirements ✅
- A README.md file, located at the root of the project folder, is mandatory.
- All scripts are tested on Ubuntu 20.04 LTS.
- Bash scripts should be exactly 3 lines long (`wc -l file` should print 3).
- All files should end with a new line and be executable.
- The first line of Bash files should be `#!/bin/bash`.
- All curl commands must use the `-s` (silent) option.
- All Python files are interpreted using python3 (version 3.8.5) and use `#!/usr/bin/python3` as the first line.
- The code adheres to PEP8 coding style (`pycodestyle version 2.8.*`).
- Documentation for modules, classes, and functions is provided using specific Python commands.
- Quiz questions and tasks' solutions are organized and located in the specified directory structure within the repository.

## Tasks Overview 📝

1. **cURL body size**
    - Bash script to fetch a URL, send a request, and display the response body's size.
    - Usage: `./0-body_size.sh 0.0.0.0:5000`

2. **cURL to the end**
    - Bash script to perform a GET request on a URL and display the response body of a 200 status code.
    - Usage: `./1-body.sh 0.0.0.0:5000/route_1`

3. **cURL Method**
    - Bash script to send a DELETE request to a given URL and display the response body.
    - Usage: `./2-delete.sh 0.0.0.0:5000/route_3`

4. **cURL only methods**
    - Bash script to display all HTTP methods accepted by a server for a given URL.
    - Usage: `./3-methods.sh 0.0.0.0:5000/route_4`

5. **cURL headers**
    - Bash script to send a GET request with a specific header and display the response body.
    - Usage: `./4-header.sh 0.0.0.0:5000/route_5`

6. **cURL POST parameters**
    - Bash script to send a POST request with specific parameters and display the response body.
    - Usage: `./5-post_params.sh 0.0.0.0:5000/route_6`

7. **Find a peak**
    - Python function to find a peak in an unsorted list of integers.

8. **Only status code**
    - Bash script to send a request and display only the status code of the response.
    - Usage: `./100-status_code.sh 0.0.0.0:5000`

9. **cURL a JSON file**
    - Bash script to send a JSON POST request with file contents and display the response body.
    - Usage: `./101-post_json.sh 0.0.0.0:5000/route_json my_json_0`

10. **Catch me if you can!**
    - Bash script to make a request that causes the server to respond with a specific message.
    - Usage: `./102-catch_me.sh`

## Author 👩‍💻
[NEAZYIT](https://github.com/NEAZYIT)
