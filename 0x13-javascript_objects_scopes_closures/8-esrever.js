#!/usr/bin/node
exports.esrever = function (list) {
  const list2 = [];
  for (let i = list.length - 1; list[i] !== undefined; i--) {
    list2.push(list[i]);
  }
  return (list2);
};
