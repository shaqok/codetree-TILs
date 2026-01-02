n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

'''
L자로 순회하도록
r = 2
c = 1
'''
r, c = 2, 1
max_sum = 0

def get_rectangle_sum(r, c):
    '''
    1. r-1, c+1 until r-2 >= 0 and c+1 < n
    2. r-1, c-1
    3. r+1, c-1 until r+2 < n and c-1 >= 0
    4. r+1, c+1
    '''
    cur_sum = 0
    cur_r, cur_c = r, c
    while True:
        cur_sum += grid[cur_r][cur_c]
        if cur_r - 1 == 0 or cur_c + 1 == n:
            break
        cur_r -= 1
        cur_c += 1
    
    while True:
        cur_r -= 1
        cur_c -= 1
        if cur_r >= 0:
            cur_sum += grid[cur_r][cur_c]
            if cur_r == 0:
                break
    
    while True:
        cur_r += 1
        cur_c -= 1
        if cur_r < n - 1 and cur_c >= 0:
            cur_sum += grid[cur_r][cur_c]
            if cur_r == n - 2 or cur_c == 0:
                break
    
    while True:
        cur_r += 1
        cur_c += 1
        if cur_r < n and cur_c < n:
            if cur_r == r and cur_c == c:
                break
            cur_sum += grid[cur_r][cur_c]
    
    return cur_sum


# for i in range(2, n):
#     for j in range(1, n-1):
#         max_sum = max(max_sum, get_rectangle_sum(i, j))
    
# print(max_sum)


# 아래로 순회
while r < n:
    max_sum = max(max_sum, get_rectangle_sum(r, c))
    r += 1

r = n - 1

while c < n - 1:
    max_sum = max(max_sum, get_rectangle_sum(r, c))
    c += 1

print(max_sum)

