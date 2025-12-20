n = int(input())
arr = [int(input()) for _ in range(n)]

'''

'''
max_count = 0
cur_count = 0

for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        max_count = max(max_count, cur_count)
        cur_count = 1
    else:
        cur_count += 1
max_count = max(max_count, cur_count)    

print(max_count)
    