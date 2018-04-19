#!/usr/bin/node

let number = process.argv[2]

console.log(isNaN(number) ? 'Not a number' : 'My number: ' + number);
