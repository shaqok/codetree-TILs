n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
MAX_LEN = 201

result = 0
grid = []

for _ in range(MAX_LEN):
    grid.append([0] * MAX_LEN)


for i in range(n):
    x_1, y_1, x_2, y_2 = x1[i] + 100, y1[i] + 100, x2[i] + 100, y2[i] + 100
    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            if grid[i][j] == 1: continue
            grid[i][j] = 1
            result += 1

print(result)