x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
MAX_LEN = 2001

grid = []
for _ in range(MAX_LEN):
    grid.append([0] * MAX_LEN)

for k in range(2):
    cur_x1, cur_x2 = x1[k] + 1000, x2[k] + 1000
    cur_y1, cur_y2 = y1[k] + 1000, y2[k] + 1000

    for i in range(cur_x1, cur_x2):
        for j in range(cur_y1, cur_y2):
            grid[i][j] = k + 1

max_width = max_height = 0

cur_x1, cur_x2 = x1[0] + 1000, x2[0] + 1000
cur_y1, cur_y2 = y1[0] + 1000, y2[0] + 1000

for i in range(cur_x1, cur_x2):
    cur_width = 0
    cur_height = 0
    for j in range(cur_y1, cur_y2):
        if grid[i][j] == 1:
            cur_width += 1
            cur_height = 1

    max_width = max(max_width, cur_width)
    max_height += cur_height

print(max_width * max_height)