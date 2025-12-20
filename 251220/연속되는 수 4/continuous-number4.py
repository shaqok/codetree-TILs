n = int(input())
arr = [int(input()) for _ in range(n)]

'''

check:
1. n = 1 -> start with 1
2. arr elements are the same -> check max again after the loop
'''

max_cnt = 1
cur_cnt = 1

for i in range(n):
    if n == 1 or arr[i] <= arr[i-1]:
        max_cnt = max(max_cnt, cur_cnt)
        cur_cnt = 1
    else:
        cur_cnt += 1

max_cnt = max(max_cnt, cur_cnt)

print(max_cnt)