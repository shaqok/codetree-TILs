const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(" ");
let a = Number(input[0]);
let b = Number(input[1]);
// Please Write your code here.

function check(a, b) {
    new_a = a;
    new_b = b;

    if (new_a > new_b) {
        new_a *= 2;
        new_b += 10;
    } else {
        new_a += 10;
        new_b *= 2;
    }

    return [new_a, new_b];
}

let arr = check(a, b);

console.log(arr[0], arr[1])

