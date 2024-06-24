#!/usr/bin/node

const args = process.argv.slice(2);

if (args.lenght <= 1) {
  console.log(0);
} else {
  const nums = args.map(Number).filter(n => !isNaN(n));
  if (nums.length <= 1) {
    console.log(0);
  } else {
    nums.sort((a, b) => b - a);
    console.log(nums[1]);
  }
}
