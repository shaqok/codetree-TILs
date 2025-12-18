x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
MAX_LEN = 2001

grid = []

for _ in range(MAX_LEN):
    grid.append([0] * MAX_LEN)

for k in range(3):
    cur_x1, cur_x2 = x1[k], x2[k]
    cur_y1, cur_y2 = y1[k], y2[k]
    for i in range(cur_x1, cur_x2):
        for j in range(cur_y1, cur_y2):
            grid[i][j] = k + 1

result = 0
min_x1, max_x2 = min(x1), max(x2)
min_y1, max_y2 = min(y1), max(y2)

for i in range(min_x1, max_x2 + 1):
    for j in range(min_y1, max_y2 + 1):
        if grid[i][j] in (1, 2):
            result += 1

print(result)

