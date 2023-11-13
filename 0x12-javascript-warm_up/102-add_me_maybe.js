#!/usr/bin/node
// This script exports a function that increments a number and calls a function

// Define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// Export the addMeMaybe function
exports.addMeMaybe = addMeMaybe;
