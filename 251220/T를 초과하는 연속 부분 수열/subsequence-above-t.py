n, t = map(int, input().split())
arr = list(map(int, input().split()))

'''
'''
max_cnt = 0
cur_cnt = 0

for i in range(n):
    # i가 0이면서 arr[i]가 t보다 크거나,
    if i == 0:
        if arr[i] > t:
            cur_cnt = 1
        else: continue
    elif arr[i] > t:
        cur_cnt += 1
    else:
        max_cnt = max(max_cnt, cur_cnt)
        cur_cnt = 0

max_cnt = max(max_cnt, cur_cnt)

print(max_cnt)