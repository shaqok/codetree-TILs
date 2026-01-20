const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, m] = input[0].split(" ").map(Number);
// Please write your code here.

function swap(a, b) {
    [a, b] = [b, a];
    return [a, b];
}

const [new_n, new_m] = swap(n, m);

console.log(new_n, new_m)