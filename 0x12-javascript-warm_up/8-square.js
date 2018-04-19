#!/usr/bin/node

arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
    console.log("Missing size");
} else {
    for (i = 0; i < arg; i++) {
	console.log(Array(arg + 1).join("X"));
    }
}
