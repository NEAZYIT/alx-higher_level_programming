# Python Network 1

This repository contains a collection of Python scripts for network operations and HTTP requests.

## Requirements
- **Allowed editors:** vi, vim, emacs
- **Platform:** Ubuntu 20.04 LTS
- **Python version:** 3.8.5
- **Tools:** pycodestyle (version 2.8.*)
- **Modules:** urllib, sys, requests
- **Execution:** All files must be executable
- **Documentation:** All modules should include documentation explaining their purpose

## Scripts
### 0-hbtn_status.py
- Fetches and displays status from [alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using urllib.

### 1-hbtn_header.py
- Retrieves and displays the value of the X-Request-Id variable in the response header using urllib and sys.

### 2-post_email.py
- Sends a POST request to a given URL with an email parameter and displays the response body (decoded in utf-8).

### 3-error_code.py
- Sends a request to a URL and handles urllib.error.HTTPError exceptions by displaying the HTTP status code.

### 4-hbtn_status.py (Using requests)
- Fetches and displays status from [alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using requests.

### 5-hbtn_header.py (Using requests)
- Retrieves and displays the value of the X-Request-Id variable in the response header using requests and sys.

### 6-post_email.py (Using requests)
- Sends a POST request to a given URL with an email parameter and displays the response body.

### 7-error_code.py (Using requests)
- Sends a request to a URL and displays the body; if HTTP status code >= 400, prints the error code.

### 8-json_api.py
- Sends a POST request to http://0.0.0.0:5000/search_user with a letter parameter and displays the response.

### 10-my_github.py
- Uses Basic Authentication with GitHub API to display the user ID.

## Usage
- Each script can be run from the command line by providing necessary arguments.
- For example: `./0-hbtn_status.py`, `./1-hbtn_header.py https://alx-intranet.hbtn.io`

## Testing
- Ensure to test each script in the provided sandbox or the specified environment.

## Author
- [NEAZYIT](https://github.com/NEAZYIT)
