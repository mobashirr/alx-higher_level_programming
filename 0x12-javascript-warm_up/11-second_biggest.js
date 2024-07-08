#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 2) { // No arguments provided
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number); // Convert arguments to numbers
  let max = -Infinity;

  for (let num of numbers) {
    if (num > max) {
      max = num;
    }
  }

  console.log(max);
}
