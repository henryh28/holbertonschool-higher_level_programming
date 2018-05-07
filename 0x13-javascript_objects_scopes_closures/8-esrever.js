#!/usr/bin/node

exports.esrever = function (list) {
  return list.map((value, index) => list[list.length - 1 - index]);
};
