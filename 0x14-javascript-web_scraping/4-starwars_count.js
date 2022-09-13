#!/usr/bin/node

const axios = require('axios');
let count = 0;
axios.get(process.argv[2]).then(
  resp => {
    for (const i of resp.data.results) {
      for (const j of i.characters) {
        if (j.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  });
