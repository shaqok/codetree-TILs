n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
grid = [0] * (n+1)

for command in commands:
    a, b = command
    for i in range(a, b+1):
        grid[i] += 1
print(max(grid))