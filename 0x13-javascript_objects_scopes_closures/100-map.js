#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);

let i = 0;
const list2 = list.map(x => x * i++);
console.log(list2);
