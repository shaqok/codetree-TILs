n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_val = 0

def get_area(k):
    return k**2 + (k+1)**2

def get_num_of_gold(r, c, k):
    return sum([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if abs(r-i) + abs(c-j) <= k
    ])


for i in range(n):
    for j in range(n):
        for k in range(2 * (n-1) + 1):
            num_of_gold = get_num_of_gold(i, j, k)

            if num_of_gold * m >= get_area(k):
                max_val = max(max_val, num_of_gold)

print(max_val)
