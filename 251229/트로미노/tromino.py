n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_sum = 0

# 블럭 1 체크
for i in range(n-2+1):
    for j in range(m-2+1):
        top_left, top_right = grid[i][j], grid[i][j+1]
        bottom_left, bottom_right = grid[i+1][j], grid[i+1][j+1]
        cur_max_sum = max((top_right + bottom_left + bottom_right), (top_left + bottom_left + bottom_right), 
            (top_left + top_right + bottom_left), (top_left + top_right + bottom_right))
        max_sum = max(max_sum, cur_max_sum)


# 블럭 2-1 체크
for i in range(n):
    for j in range(m-3+1):
        cur_sum = sum(grid[i][j:j+3])
        max_sum = max(max_sum, cur_sum)

# 블럭 2-2 체크
for i in range(n-3+1):
    for j in range(m):
        cur_sum = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        max_sum = max(max_sum, cur_sum)

print(max_sum)
