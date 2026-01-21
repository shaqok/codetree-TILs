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

const nextGrid = Array(n).fill().map(() => Array(n).fill(0));
let newR = r - 1;
let newC = c - 1;

function inBombRange(x, y, centerX, centerY, bombRange) {
    return (x === centerX || y === centerY) && 
           (Math.abs(x - centerX) + Math.abs(y - centerY) < bombRange);
}

function bomb(centerX, centerY) {
    const bombRange = grid[centerX][centerY];

    // 0으로 처리
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (inBombRange(i, j, centerX, centerY, bombRange)) {
                grid[i][j] = 0;
            }
        }   
    }

    // nextGrid에 변화 저장
    for (let j = 0; j < n; j++) {
        let nextRow = n - 1;
        for (let i = n - 1; i >= 0; i--) {
            if (grid[i][j]) {
                nextGrid[nextRow][j] = grid[i][j];
                nextRow -= 1;
            }
        }
    }

    // grid 로 다시 저장
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            grid[i][j] = nextGrid[i][j];
        }
    }
}

bomb(newR, newC);

for (let row of grid) {
    console.log(row.join(" "));
}