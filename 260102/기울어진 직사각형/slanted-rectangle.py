n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    cur_sum = 0

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy

            if not in_range(x, y):
                return 0
            
            cur_sum += grid[x][y]
    
    return cur_sum

max_sum = 0

for i in range(2, n):
    for j in range(1, n):
        for k in range(1, n):
            for l in range(1, n):
                max_sum = max(max_sum, get_score(i, j, k, l))

print(max_sum)