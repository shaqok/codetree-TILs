n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
RED = 1
BLUE = 2
MAX_LEN = 202
grid = []
for _ in range(MAX_LEN):
    grid.append([0] * MAX_LEN)

N = len(x1)

for k in range(N):
    cur_x1, cur_y1, cur_x2, cur_y2 = x1[k] + 100, y1[k] + 100, x2[k] + 100, y2[k] + 100
    for i in range(cur_x1, cur_x2):
        for j in range(cur_y1, cur_y2):
            if k % 2 == 0:
                grid[i][j] = RED
            else:
                grid[i][j] = BLUE

result = 0

for i in range(MAX_LEN):
    for j in range(MAX_LEN):
        if grid[i][j] == BLUE:
            result += 1

print(result)