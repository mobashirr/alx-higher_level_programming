#!/usr/bin/node


// parameters of the program
const { argv } = require('node:process');

let length = argv.reduce((acc, _) => acc + 1, 0);

switch (length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log(process.argv[3-1]);
    break;
  default:
    console.log('Arguments found');
}
