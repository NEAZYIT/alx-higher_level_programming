#!/usr/bin/node

// Get the first argument from the command line
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const num = parseInt(arg);

// Check if the conversion resulted in a valid integer
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
