#!/usr/bin/node
// factorial with js:

function factorial (number) {
  if (number <= 0 || isNaN(number)) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

const { argv } = require('node:process');

console.log(factorial(argv[2]));
