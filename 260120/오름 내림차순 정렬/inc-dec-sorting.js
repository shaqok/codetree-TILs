const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = parseInt(input[0]);
const nums = input[1].split(' ').map(Number);

// Please Write your code here.
nums.sort((prev, cur) => {
    if (prev < cur) {
        return -1;
    } else if (prev > cur) {
        return 1;
    }
    return 0;
})

console.log(nums.join(" "));

nums.sort((prev, cur) => cur - prev);

console.log(nums.join(" "));