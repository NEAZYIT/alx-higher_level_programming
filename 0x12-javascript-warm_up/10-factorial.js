#!/usr/bin/node
// This script computes and prints the factorial of a number

// Get the number from the command-line arguments
const num = process.argv[2];

// Define the factorial function
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Print the factorial of the number
console.log(factorial(Number(num)));
