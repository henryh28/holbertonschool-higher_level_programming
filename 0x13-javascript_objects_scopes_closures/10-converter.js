#!/usr/bin/node

exports.converter = function (base) {
  return function converterFunction (param) {
    return param.toString(base);
  };
};

// Ref: https://blog.ashryan.io/converting-base-10-binary-javascript/
