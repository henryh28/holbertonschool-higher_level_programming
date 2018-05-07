#!/usr/bin/node

const request = require('request');
let total = 0;

request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);

  for (let film of JSON.parse(body).results) {
    for (let character of film.characters) {
      if (character.includes('18')) total++;
    }
  }
  console.log(total);
});
