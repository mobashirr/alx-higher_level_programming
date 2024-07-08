#!/usr/bin/node

function isNumeric (value) {
  return !isNaN(Number(value));
}

const { argv } = require('node:process');

if (isNumeric(argv[2])) {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('#'.repeat(argv[2]));
  }
} else {
  console.log('Missing size');
}
