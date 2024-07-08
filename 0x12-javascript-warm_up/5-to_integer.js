#!/usr/bin/node

function isNumeric (value) {
  return !isNaN(Number(value));
}

// parameters of the program
const { argv } = require('node:process');

if (isNumeric(argv[2])) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
