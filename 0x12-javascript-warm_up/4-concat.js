#!/usr/bin/node
// print two arg given to the programs
// parameters of the program
const { argv } = require('node:process');

switch (argv.length) {
  default:
    console.log(process.argv[3 - 1] + ' is ' + process.argv[4 - 1]);
}
