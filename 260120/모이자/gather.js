const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);

// Please Write your code here.

let minVal = Number.MAX_SAFE_INTEGER;
for (let i = 0; i < n; i++) {
    let curVal = 0;
    for (let j = 0; j < n; j++) {
        if (i !== j) {
            curVal += Math.abs(i - j) * arr[j];
        }
    }
    minVal = curVal > minVal ? minVal : curVal;
}

console.log(minVal);