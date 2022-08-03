#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let result = 0;

  for (let i = 0; list[i] !== undefined; i++) {
    if (list[i] === searchElement) {
      result = result + 1;
    }
  }

  return (result);
};
