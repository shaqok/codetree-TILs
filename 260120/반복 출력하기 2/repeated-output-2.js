const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);

// Please Write your code here.
function recur(n) {
    if (n == 0) {
        return
    }
    console.log("HelloWorld");
    recur(n-1);
}

recur(n);