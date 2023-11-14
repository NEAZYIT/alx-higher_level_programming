#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    // Call the constructor of the parent class (Square5) using super()
    super(size);
  }

  charPrint (c) {
    // If c is undefined, use the character 'X'; otherwise, use the specified character
    const char = c || 'X';

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
