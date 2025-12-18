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

    for i in range(cur_x1, cur_x2 + 1):
        for j in range(cur_y1, cur_y2 + 1):
            grid[i][j] = k + 1


cur_x1, cur_x2 = x1[0] + 1000, x2[0] + 1000
cur_y1, cur_y2 = y1[0] + 1000, y2[0] + 1000

# for i in range(x1[1] + 1000, x2[1] + 1000):
#     # for j in range(cur_y1, cur_y2):
#     print(grid[i][cur_y1:cur_y2])

min_height = cur_x1
max_height = cur_x1

max_width_len = 0

for i in range(cur_x1, cur_x2 + 1):
    width_count = 0
    cur_min_width = cur_y1
    cur_max_width = cur_y1
    for j in range(cur_y1, cur_y2 + 1):
        if width_count == 0 and grid[i][j] == 1:
            cur_min_width = j
            cur_max_width = j
            width_count += 1
        elif grid[i][j] == 1:
            cur_max_width = j
            width_count += 1
    if 1 in set(grid[i]):
        max_height = i
    
    max_width_len = max(max_width_len, (cur_max_width - cur_min_width))

print(max_width_len * (max_height - min_height))

'''
5 5 15 15
3 9 18 12
'''