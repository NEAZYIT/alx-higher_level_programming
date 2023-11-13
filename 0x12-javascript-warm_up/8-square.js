#!/usr/bin/node
// This script prints a square of size 'size' using the character 'X'

// Get the size of the square from the command-line arguments
const size = process.argv[2];

// Check if the size can be converted to a number
if (isNaN(size)) {
  // If not, print an error message
  console.log('Missing size');
} else {
  // If so, print a square of size 'size'
  for (let i = 0; i < Number(size); i++) {
    console.log('X'.repeat(Number(size)));
  }
}
