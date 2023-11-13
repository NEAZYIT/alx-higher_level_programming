#!/usr/bin/node

// Get the number of times to print "C is fun" from the command line argument
const x = parseInt(process.argv[2]);

// Check if x is a valid number
if (!isNaN(x) && x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
