const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m, q] = input[0].split(' ').map(Number);
const building = input.slice(1, 1 + n).map(line => line.split(' ').map(Number));
const winds = input.slice(1 + n, 1 + n + q).map(line => {
  const [r, d] = line.split(' ');
  return [Number(r), d];
});

// Please write your code here.
const LEFT = 0;
const RIGHT = 1;

function shift(row, dir) {
    if (dir === LEFT) {
        // 첫번째 값을 맨뒤로 삽입
        let temp = building[row][0];
        for (let col = 0; col < m-1; col++) {
            building[row][col] = building[row][col+1];
        }
        building[row][m-1] = temp;
    } else {
        // 맨 뒤의 값을 첫번째에 삽입
        let temp = building[row][m-1];
        for (let col = m-1; col >= 1; col--) {
            building[row][col] = building[row][col-1];
        }
        building[row][0] = temp;        
    }
}

function hasMatch(row1, row2) {
    for (let i = 0; i < m; i++) {
        if (building[row1][i] === building[row2][i]) return true;
    }
    return false;
}

function flip(curFlip) {
    return curFlip === LEFT ? RIGHT : LEFT;
}

function simulate(startRow, startDir) {
    shift(startRow, startDir);

    startDir = flip(startDir);

    // check upper
    for (let row = startRow, dir = startDir; row-1 >= 0; row--) {
        if (hasMatch(row, row-1)) {
            shift(row - 1, dir);
            dir = flip(dir);
        } else break;
    }

    // check down
    for (let row = startRow, dir = startDir; row+1 < n; row++) {
        if (hasMatch(row, row+1)) {
            shift(row + 1, dir);
            dir = flip(dir);
        } else break;
    }
}

winds.forEach(([r, d]) => {
    simulate(r - 1, d === 'L' ? RIGHT : LEFT)
});

for (let row = 0; row < n; row++) {
    console.log(building[row].join(' '));
}