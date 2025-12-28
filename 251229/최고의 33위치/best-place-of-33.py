n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnt = 0

# m = 6, 0 1 2 3 4 5
m = 3
for i in range(n-m+1):
    for j in range(n-m+1):
        first_row_sum = sum(grid[i][j:j+m])
        second_row_sum = sum(grid[i+1][j:j+m])
        thrid_row_sum = sum(grid[i+2][j:j+m])
        cur_cnt = first_row_sum + second_row_sum + thrid_row_sum
        max_cnt = max(max_cnt, cur_cnt)

print(max_cnt)
