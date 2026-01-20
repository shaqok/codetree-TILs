const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const str = input[0];
// Please Write your code here.

n = str.length;
half_n = Math.floor(n / 2);

function checkPalindrome(str) {
    for (let i = 0; i < half_n; i++) {
        if (str[i] !== str[n-1-i]) {
            return "No"
        }
    }
    return "Yes"
}

console.log(checkPalindrome(str))