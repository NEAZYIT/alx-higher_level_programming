# JavaScript Warm-Up

This repository contains a set of JavaScript scripts to get started with the basics of JavaScript. The scripts are designed to be executed on Ubuntu 20.04 LTS using Node.js (version 14.x).

## Requirements ⚙️

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable

## More Info

### Install Node 14 🔧

To install Node.js version 14, use the following commands:

```shell
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard

To install the semistandard package globally, use the following command:

```shell
$ sudo npm install semistandard --global
```

## Tasks ✅

### First constant, first print

- Create a constant variable called `myVar` with the value "JavaScript is amazing."
- Use `console.log(...)` to print all output.

### 3 languages

- Print three lines: "C is fun," "Python is cool," and "JavaScript is amazing."
- Use `console.log(...)` to print all output.

### Arguments

- Print a message depending on the number of arguments passed:
  - If no arguments are passed to the script, print "No argument."
  - If only one argument is passed to the script, print "Argument found."
  - Otherwise, print "Arguments found."
- Use `console.log(...)` to print all output.

### Value of my argument

- Print the first argument passed to the script.
- If no arguments are passed to the script, print "No argument."
- Use `console.log(...)` to print all output.

### Create a sentence

- Print two arguments passed to the script in the format " is ".
- Use `console.log(...)` to print all output.

### An Integer

- Print "My number: <first argument converted to an integer>" if the first argument can be converted to an integer.
- If the argument can't be converted to an integer, print "Not a number."
- Use `console.log(...)` to print all output.

### Loop to languages

- Print three lines ("C is fun," "Python is cool," "JavaScript is amazing") using an array of strings and a loop.
- Use only one `console.log`.
- Use a loop (while, for, etc.).

### I love C

- Print "C is fun" x times, where x is the first argument of the script.
  - If the first argument can't be converted to an integer, print "Missing number of occurrences."
- Use only two `console.log`.
- Use a loop (while, for, etc.).

### Square

- Print a square using "X."
- The first argument is the size of the square.
  - If the first argument can't be converted to an integer, print "Missing size."
- Use `console.log(...)` to print all output.

### Factorial

- Compute and print the factorial of the first argument.
  - If no arguments are passed to the script, print "1."
  - If the argument can't be converted to an integer, print "1."
- Use a recursive function.
- Use a function.
- Use `console.log(...)` to print all output.

### Second biggest!

- Search for the second biggest integer in the list of arguments.
  - If no arguments are passed, print "0."
  - If the number of arguments is 1, print "0."
- Use `console.log(...)` to print all output.

### Object

- Replace the value "12" with "89" in the given object.
- Use `console.log(...)` to print all output.

### Add file

- Write a function that returns the addition of two integers.
- The function is visible from outside and is named `add`.
- Use `console.log(...)` to print all output.

### Usage 📋

Each task is a separate JavaScript script file that you can run. For example, to run the first task:

```shell
$ ./0-javascript_is_amazing.js
```
Replace the filename with the task you want to execute.

### Author 👤

[NEAZYIT](https://github.com/NEAZYIT)
