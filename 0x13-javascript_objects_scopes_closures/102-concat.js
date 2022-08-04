#!/usr/bin/node
const fs = require("fs");

let Atext = fs.readFileSync(process.argv[2], 'utf-8');
let Btext = fs.readFileSync(process.argv[3], 'utf-8');

fs.writeFileSync(process.argv[4], Atext + Btext, 'utf-8');
