#!/usr/bin/node

let number = parseInt(process.argv[2]);

function factorial (n) {
  return (isNaN(n) || n <= 1 ? 1 : n * factorial(n - 1));
}

console.log(factorial(number));
