const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [R, C] = input[0].split(' ').map(Number);
const grid = input.slice(1).map(line => line.trim().split(' '));

// Please Write your code here.
let total_cnt = 0;

for (let k = 1; k < R-1; k++) {
    for (let l = 1; l < C-1; l++) {
        for (let n = k + 1; n < R; n++) {
            for (let m = l + 1; m < C; m++) {
                let firstMove = grid[k][l];
                let secondMove = grid[n][m];
                if (grid[0][0] !== firstMove && firstMove !== secondMove && (n !== R-1 && m !== C-1)) {
                    total_cnt++;
                }
            }
        }
    }
}
console.log(total_cnt);