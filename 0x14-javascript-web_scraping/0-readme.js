#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, data) {
  error ? console.log(error) : console.log(data);
});

// Ref: https://stackoverflow.com/questions/9168737/read-a-text-file-using-node-js
