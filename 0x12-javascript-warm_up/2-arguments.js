#!/usr/bin/node

// Get the number of arguments passed
const numArgs = process.argv.length - 2; // Subtract 2 to account for 'node' and the script name

// Check the number of arguments and print the appropriate message
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
