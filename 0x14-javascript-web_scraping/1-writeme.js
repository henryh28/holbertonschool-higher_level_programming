#!/usr/bin/node

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (error, data) {
  if (error) console.log(error);
});

// Ref: https://stackoverflow.com/questions/2496710/writing-files-in-node-js
