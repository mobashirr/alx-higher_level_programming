#!/usr/bin/node


// parameters of the program
const { argv } = require('node:process');

switch (argv.length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log(process.argv[3-1]);
    break;
  default:
    console.log('Arguments found');
}
