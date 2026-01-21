const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const blocks = input.slice(1, n + 1).map(Number);
const [s1, e1] = input[n + 1].split(' ').map(Number);
const [s2, e2] = input[n + 2].split(' ').map(Number);

// Please write your code here.
// let temp = new Array(n).fill(0);
let result = [...blocks];
let temp = [];

// first iteration
for (let i = s1 - 1; i < e1; i++) {
    result[i] = -1;
}

for (let i = 0; i < n; i++) {
    if (result[i] !== -1) {
        temp.push(result[i])
    }
}
result = temp;
temp = [];
// scond deletion
for (let i = s2 - 1; i < e2; i++) {
    result[i] = -1;
}

for (let i = 0; i < result.length; i++) {
    if (result[i] !== -1) {
        temp.push(result[i])
    }
}
result = temp;

console.log(result.length);
for (let block of result) {
    console.log(block);
}