const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
let [a, b] = input[0].split(" ").map(Number);
// Please Write your code here.

function func(a, b) {
    let new_a = a;
    let new_b = b;
    if (a > b) {
        new_a += 25;
        new_b *= 2;
    } else {
        new_b += 25;
        new_a *= 2;
    }
    return [new_a, new_b];
}

let result = func(a, b);
console.log(result[0], result[1]);