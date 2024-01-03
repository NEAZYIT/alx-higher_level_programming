# Javascript Web Scraping

## Description
This repository contains scripts written in JavaScript for performing various web scraping tasks. The scripts utilize Node.js and external modules for handling different functionalities.

## Requirements
- The scripts are to be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of each file should be `#!/usr/bin/node`
- The repository must contain a `README.md` file at the root
- Code should adhere to the semistandard rules with semicolons on top and follow the AirBnB style
- All files must be executable

## Installation Instructions
### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard
```bash
$ sudo npm install semistandard --global
```

### Install request module
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks
Task 0: Readme
Script that reads and prints the content of a file.

Task 1: Write me
Script that writes a string to a file.

Task 2: Status code
Script that displays the status code of a GET request.

Task 3: Star wars movie title
Script that prints the title of a Star Wars movie based on the movie ID.

Task 4: Star wars Wedge Antilles
Script that prints the number of movies where the character “Wedge Antilles” is present.

Task 5: Loripsum
Script that gets the contents of a webpage and stores it in a file.

Task 6: How many completed?
Script that computes the number of tasks completed by user id.

## Usage
Each task has its own JavaScript file which can be run with Node.js. For example:
```bash
$ node 0-readme.js cisfun
$ node 1-writeme.js my_file.txt "Python is cool"
$ node 2-statuscode.js https://alx-intranet.hbtn.io/status
...
```

## Author
[NEAZYIT](https://github.com/NEAZYIT)
