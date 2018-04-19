#!/usr/bin/node

nums = process.argv.slice(2).sort();
nums.length > 1 ? console.log(nums[nums.length - 2]) : console.log(0);
