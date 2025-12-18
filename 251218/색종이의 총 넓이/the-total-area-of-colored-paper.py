n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# square length of 8
MAX_LEN = 201
SQUARE_LEN = 8

grid = []
for _ in range(MAX_LEN):
    grid.append([0] * MAX_LEN)

result = 0

for k in range(n):
    cur_x, cur_y = x[k] + 100, y[k] + 100
    for i in range(cur_x, cur_x + SQUARE_LEN):
        for j in range(cur_y, cur_y + SQUARE_LEN):
            if grid[i][j] == 1: continue
            grid[i][j] = 1
            result += 1

print(result)
