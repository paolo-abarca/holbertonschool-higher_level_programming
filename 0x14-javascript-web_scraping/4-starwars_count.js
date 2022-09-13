#!/usr/bin/node

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;
axios.get(process.argv[2]).then(
  resp => {
    for (const i of resp.data.results) {
      for (const j of i.characters) {
        if (j === url) {
          count++;
        }
      }
    }
    console.log(count);
  });
