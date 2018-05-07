#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = 0;

  list.forEach(function (i) {
    if (i === searchElement) {
      result++;
    }
  });

  return result;
};
