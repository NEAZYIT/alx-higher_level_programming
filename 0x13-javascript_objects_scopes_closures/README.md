# 0x13. JavaScript - Objects, Scopes and Closures 

## Requirements 📌

- **General**
  - Allowed editors: vi, vim, emacs
  - Files interpreted on Ubuntu 20.04 LTS using node (version 14.x)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/node`
  - A README.md file at the root of the project folder is mandatory
  - Code should be semistandard compliant (Rules of Standard + semicolons on top, AirBnB style as reference)
  - All files must be executable
  - Length of files will be tested using `wc`
  - Not allowed to use `var`

- **More Info**
  - Install Node 14:
    ```bash
    $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```
  - Install semi-standard:
    ```bash
    $ sudo npm install semistandard --global
    ```

## Tasks 📋

### Task 0: Rectangle #0
- Write an empty class `Rectangle` that defines a rectangle.
- Use the class notation for defining the class.

### Task 1: Rectangle #1
- Write a class `Rectangle` that defines a rectangle.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attributes `width` and `height`.

### Task 2: Rectangle #2
- Write a class `Rectangle` that defines a rectangle.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attributes `width` and `height`.
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

### Task 3: Rectangle #3
- Write a class `Rectangle` that defines a rectangle.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attributes `width` and `height`.
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
- Create an instance method `print()` that prints the rectangle using the character 'X'.

### Task 4: Rectangle #4
- Write a class `Rectangle` that defines a rectangle.
- Constructor must take 2 arguments `w` and `h`.
- Initialize instance attributes `width` and `height`.
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
- Create instance methods `print()`, `rotate()`, and `double()`.

### Task 5: Square #0
- Write a class `Square` that defines a square and inherits from `Rectangle` of 4-rectangle.js.
- Constructor must take 1 argument `size`.

### Task 6: Square #1
- Write a class `Square` that defines a square and inherits from `Square` of 5-square.js.
- Create an instance method `charPrint(c)` that prints the rectangle using the character `c`.

### Task 7: Occurrences
- Write a function that returns the number of occurrences in a list.
- Prototype: `exports.nbOccurences = function (list, searchElement)`.

### Task 8: Esrever
- Write a function that returns the reversed version of a list.
- Prototype: `exports.esrever = function (list)`.

### Task 9: Log me
- Write a function that prints the number of arguments already printed and the new argument value.
- Prototype: `exports.logMe = function (item)`.

### Task 10: Number conversion
- Write a function that converts a number from base 10 to another base passed as an argument.
- Prototype: `exports.converter = function (base)`.

## Usage 🚀

To run the tasks, execute the following commands:

```bash
$ ./0-main.js
$ ./1-main.js
...
$ ./10-main.js
```
## Testing 🧪

If there are any test scripts or instructions for testing, include them in this section.

```bash
$ npm test
```

## Troubleshooting 🚨

### Installation Issues 🗺️

- **Problem:** If you encounter issues with installing Node.js 14:
  - **Solution:** Ensure that you have the necessary permissions to run the installation commands with `sudo`. If problems persist, you can visit [NodeSource](https://deb.nodesource.com/) for additional support.

- **Problem:** Unable to install the `semistandard` package globally:
  - **Solution:** Confirm that Node.js is successfully installed, and you have an internet connection. Retry the installation command, and check for any error messages. If the problem persists, consult the [npm documentation](https://docs.npmjs.com/) for troubleshooting.

### Running Tasks Issues  🚧 

- **Problem:** Script execution permission denied:
  - **Solution:** Make sure all your script files have the correct execution permissions. You can use the `chmod` command to grant execution rights:
    ```bash
    $ chmod +x 0-main.js
    $ chmod +x 1-main.js
    # Repeat for other script files
    ```

- **Problem:** Tasks not producing expected output:
  - **Solution:** Check the console for error messages or unexpected behavior. Ensure that you are using the correct Node.js version (14.x) and that all dependencies are installed. Review the README.md for any task-specific instructions.

- **Problem:** Issues related to environment or dependencies:
  - **Solution:** Confirm that your environment meets the specified requirements. If needed, refer to the installation section for guidance. Make sure to install any additional dependencies mentioned in the README.

These are just examples, and you should tailor the troubleshooting section based on the actual issues users might encounter in your specific project. Providing clear and actionable solutions can significantly improve the user experience and reduce the number of support requests.

## Authors 👤

- [NEAZYIT](https://github.com/NEAZYIT)