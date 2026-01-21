const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
let A = input[0];

/**
 * n-1 번 만큼 shift를 진행하며
 * runLengthEncoding을 실행
 * 길이를 체크해서 최소 길이로 업데이트
 */

const n = A.length
let minVal = Number.MAX_SAFE_INTEGER;

function runLengthEnc(str) {
    let result = '';
    let curCount = 1;
    for (let i = 0; i < n; i++) {
        if (i === n - 1 || str[i] !== str[i+1]) {
            result += `${str[i]}${curCount}`;
            curCount = 1;
        } else {
            curCount += 1;
        }
    }
    return result;
}

for (let i = 0; i < n; i++) {
    let arr = A.split('');
    let temp = arr.shift();
    arr.push(temp);
    A = arr.join("");
    let encodedA = runLengthEnc(A);
    minVal = Math.min(minVal, encodedA.length);
}

console.log(minVal);