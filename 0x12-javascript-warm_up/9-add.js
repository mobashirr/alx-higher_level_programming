#!/usr/bin/node

function add (n1, n2) {
  return (n1 + n2);
}

const { argv } = require('node:process');

console.log(add(Number(argv[2]), Number(argv[3])));
