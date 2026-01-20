const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const A = input[0];
// Please Write your code here.


function check_str(str){
    let hashMap = {};

    for (let i = 0; i < A.length; i++) {
        if (A[i] in hashMap) {
            hashMap[A[i]] += 1;
        } else {
            hashMap[A[i]] = 1;
        }
    }

    if (Object.keys(hashMap).length >= 2) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}

check_str(A)