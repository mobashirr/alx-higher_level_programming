#!/usr/bin/node
// this program takes array of parameters from process.arg
// and display messege depending on length of the array

// parameters of the program
const { argv } = require('node:process');

switch (argv.length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
