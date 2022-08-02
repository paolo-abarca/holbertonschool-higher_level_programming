#!/usr/bin/node
function add (a, b) {
  console.log(Number(a) + Number(b));
}

const first = process.argv[2];
const second = process.argv[3];
add(first, second);
