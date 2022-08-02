#!/usr/bin/node
const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= size; i++) {
    let row = '';

    for (let j = 1; j <= size; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
