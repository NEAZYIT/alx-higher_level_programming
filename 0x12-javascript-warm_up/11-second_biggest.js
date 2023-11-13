#!/usr/bin/node
// This script finds and prints the second biggest integer in the list of command-line arguments

// Get the arguments and convert them to numbers
const args = process.argv.slice(2).map(Number);

// Check the number of arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the numbers in descending order
  args.sort((a, b) => b - a);
  // Print the second biggest number
  console.log(args[1]);
}
