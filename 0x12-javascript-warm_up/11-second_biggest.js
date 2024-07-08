#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  var big = Number(argv[2]);
  for (let i = 2; i < argv.length; i++) {
    if (isNaN(argv[i])) {
      continue;
    } else if (big < Number(argv[i])) {
      big = Number(argv[i]);
    }
  }
  console.log(big);
}
