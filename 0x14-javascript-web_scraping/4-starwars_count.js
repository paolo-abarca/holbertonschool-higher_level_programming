#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2]).then(
  resp => {
    const url = resp.data.results[0].characters[15];
    axios.get(url).then(
      result => {
        console.log(result.data.films.length);
      });
  });
