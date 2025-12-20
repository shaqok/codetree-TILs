N = int(input())
arr = [int(input()) for _ in range(N)]

'''
condition arr[i] > 0 or not
1. check n = 1
2. check all(arr) the same == True
'''
max_count = 1
cur_count = 1
for i in range(N):
    if i == 0 or (arr[i] > 0 and arr[i-1] < 0) or (arr[i] < 0 and arr[i-1] > 0):
        max_count = max(max_count, cur_count)
        cur_count = 1
    else:
        cur_count += 1
max_count = max(max_count, cur_count)

print(max_count)
