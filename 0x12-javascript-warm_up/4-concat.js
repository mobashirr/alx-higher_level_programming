#!/usr/bin/node
// print two arg given to the program 
// parameters of the program
const { argv } = require('node:process');

switch (argv.length) {
  case 2:
    console.log('No argument');
    break;
  default:
    console.log(process.argv[3 - 1] + ' is ' + process.argv[4 - 1]);
}
