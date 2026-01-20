const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

// Please Write your code here.
function func_abs(arr) {
    for (let i = 0; i < n; i++) {
        arr[i] = Math.abs(arr[i])
    }
}

func_abs(arr)

console.log(arr.join(" "))