n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


def check_pos(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[i][j] < 0:
                return False
    
    return True

def get_count(x1, y1, x2, y2):
    return (x2 - x1 + 1) * (y2 - y1 + 1)

max_num = 0

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if check_pos(i, j, k, l):
                    cur_sum = get_count(i, j, k, l)
                    max_num = max(max_num, cur_sum)


print(max_num)
                    
