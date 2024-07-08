#!/usr/bin/node

function add (n1, n2) {
  return (n1 + n2);
}

const { argv } = require('node:process');

add(argv[2], argv[3]);
