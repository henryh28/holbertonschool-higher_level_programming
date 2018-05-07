#!/usr/bin/node

const request = require('request');
const endpoint = 'http://swapi.co/api/films/' + process.argv[2];

request(endpoint, function (error, response, body) {
  error ? console.log(error) : console.log(JSON.parse(body)['title']);
});
