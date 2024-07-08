#!/usr/bin/node

function isNumeric (value) {
  return !isNaN(Number(value));
}

const messege = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const { argv } = require('node:process');

if (isNumeric(argv[2])) {
  // if the given arg is valid number:
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log(messege[0]);
  }
} else {
  console.log('Missing number of occurrences');
}
