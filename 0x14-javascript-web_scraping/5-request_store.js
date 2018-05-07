#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  error ? console.log(error) : fs.writeFile(process.argv[3], body, 'utf8');
});
