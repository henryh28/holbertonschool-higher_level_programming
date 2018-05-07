#!/usr/bin/node
const SquareV1 = require('./5-square');

module.exports = class Square extends SquareV1 {
  charPrint (c) {
    c === undefined ? this.print() : this.print(c);
  }
};
