#!/usr/bin/node

const fs = require('fs');
const axios = require('axios');

axios.get(process.argv[2]).then(
  resp => {
    const result = resp.data;
    fs.writeFile(process.argv[3], result, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  });
