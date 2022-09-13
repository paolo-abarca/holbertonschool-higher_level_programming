#!/usr/bin/node

const axios = require('axios');

const users = 'https://jsonplaceholder.typicode.com/users/';

axios.get(users).then(
  resp => {
    const totalusers = resp.data.length;
    const dict = {};

    axios.get(process.argv[2] + '?completed=true').then(
      resp2 => {
        const alltask = resp2.data.length;

        for (let iduser = 1; iduser <= totalusers; iduser++) {
          let taskcom = 0;
          for (let iterator = 0; iterator < alltask; iterator++) {
            if (resp2.data[iterator].userId === iduser) {
              taskcom++;
            }
          }
          dict[iduser] = taskcom;
        }
        console.log(dict);
      });
  });
