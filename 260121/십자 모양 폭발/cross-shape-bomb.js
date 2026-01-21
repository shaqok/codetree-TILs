const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const grid = input.slice(1, 1 + n).map(line => line.split(' ').map(Number));
const [r, c] = input[1 + n].split(' ').map(Number);

/**
 * 1. 범위 계산 -> 격자 안에서 범위에 해당하는 곳은 -1로 처리
 * 2. 삭제 처리 -> 열로 계산하면서 -1인 곳은 제외하고 새로 값을 처리
 *  현재 길이가 n 보다 작은 경우 0으로 채우기
 */

// 범위 계산 - 행
let newR = r - 1;
let newC = c - 1;
let power = grid[newR][newC] - 1;

for (let i = newR - power; i < newR + power + 1; i++) {
    if (0 <= i && i < n) {
        grid[i][newC] = -1
    }
}
// 범위 계산 - 열
for (let i = newC - power; i < newC + power + 1; i++) {
    if (0 <= i && i < n) {
        grid[newR][i] = -1
    }
}

// 2. 삭제 처리 -> 열로 계산하면서 -1인 곳은 제외하고 새로 값을 처리
//  현재 길이가 n 보다 작은 경우 0으로 채우기
for (let i = 0; i < n; i++) {
    let temp = [];
    for (let j = n-1; j >= 0; j--) {
        if (grid[j][i] !== -1) {
            temp.push(grid[j][i]);
        }
    }

    for (let k = temp.length; k < n; k++) {
        temp.push(0);
    }

    for (let k = n-1; k >= 0; k--) {
        grid[k][i] = temp[n-k-1];
    }
}

for (let row of grid) {
    console.log(row.join(" "));
}