#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) { // No arguments or only one argument provided
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number); // Convert arguments to numbers
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let num of numbers) {
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
