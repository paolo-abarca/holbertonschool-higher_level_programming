#!/usr/bin/node

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]).then(
  resp => {
    const list = resp.data.characters;
    list.forEach((item) => {
      axios.get(item).then(
        resp2 => {
          console.log(resp2.data.name);
        });
    });
  });
