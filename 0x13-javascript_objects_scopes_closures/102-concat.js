#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [fileA, fileB, fileC] = args;

try {
  const contentA = fs.readFileSync(fileA, 'utf-8');
  const contentB = fs.readFileSync(fileB, 'utf-8');

  const concatenatedContent = contentA + contentB;

  fs.writeFileSync(fileC, concatenatedContent);

  console.log(`The content of ${fileA} and ${fileB} has been concatenated and saved to ${fileC}`);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
