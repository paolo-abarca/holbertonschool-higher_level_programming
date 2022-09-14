#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2] + '?completed=true').then(
  resp => {
    const dict = {};
    resp.data.forEach((item) => {
      if (dict[item.userId] !== undefined) {
        dict[item.userId] += 1;
      } else {
        dict[item.userId] = 1;
      }
    });
    console.log(dict);
  });
