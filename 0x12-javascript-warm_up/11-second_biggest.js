#!/usr/bin/node
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  const list = [];

  for (let i = 2; process.argv[i] !== undefined; i++) {
    list.push(Number(process.argv[i]));
  }

  list.sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}
