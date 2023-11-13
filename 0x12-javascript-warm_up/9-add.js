#!/usr/bin/node
// This script prints the addition of two integers

// Get the integers from the command-line arguments
const a = process.argv[2];
const b = process.argv[3];

// Define the add function
function add (a, b) {
  return Number(a) + Number(b);
}

// Print the result of the addition
console.log(add(a, b));
