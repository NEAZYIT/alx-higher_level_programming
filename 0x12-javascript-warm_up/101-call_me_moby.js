#!/usr/bin/node
// This script exports a function that executes a function x times

// Define the callMeMoby function
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function
exports.callMeMoby = callMeMoby;
