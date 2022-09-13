#!/usr/bin/node

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]).then(
  resp => {
    console.log(resp.data.title);
  });
