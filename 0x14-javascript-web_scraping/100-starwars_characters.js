#!/usr/bin/node

const request = require('request');
const endpoint = 'http://swapi.co/api/films/' + process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) console.log(error);

  for (let i = 0; i < JSON.parse(body).characters.length; i++) {
    request(JSON.parse(body).characters[i], function (newError, newResponse, newBody) {
      console.log(JSON.parse(newBody).name);
    });
  }
});
