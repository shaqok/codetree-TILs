n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr = [0] * 2000
# arr = [0] * 2000

cur_pos = 1000
prev_dir = None
# cur_pos = 1000

for i in range(n):
    cur_x, cur_dir = x[i], dir[i]

    if cur_dir == 'R':
        if prev_dir == 'R':
            cur_pos += 1

        for j in range(cur_pos, cur_pos + cur_x):
            arr[j] += 1
        cur_pos = cur_pos + cur_x - 1
        prev_dir = cur_dir
    else:
        if prev_dir == 'L':
            cur_pos -= 1

        for j in range(cur_pos, cur_pos - cur_x, -1):
            arr[j] += 1
        cur_pos = cur_pos - cur_x + 1
        prev_dir = cur_dir

counts = [val for val in arr if val >= 2]
print(len(counts))
    
