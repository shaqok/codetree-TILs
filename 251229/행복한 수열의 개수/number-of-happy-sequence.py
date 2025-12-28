n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dict를 사용: 각 row, col의 숫자개수를 카운트
# 루프가 끝날때 m을 만족하는 수가 있다면 cnt + 1

cnt = 0
for i in range(n):
    # row
    max_happy_cnt = 0
    happy_cnt = 1
    for j in range(1, n):
        # consecutive same values
        if grid[i][j] != grid[i][j-1]:
            max_happy_cnt = max(max_happy_cnt, happy_cnt)
            happy_cnt = 1
        elif grid[i][j] == grid[i][j-1]:
            happy_cnt += 1
    max_happy_cnt = max(max_happy_cnt, happy_cnt)
    if max_happy_cnt >= m:
        cnt += 1

    # col
    max_happy_cnt = 0
    happy_cnt = 1
    for j in range(1, n):
        # consecutive same values
        if grid[j][i] != grid[j-1][i]:
            max_happy_cnt = max(max_happy_cnt, happy_cnt)
            happy_cnt = 1
        elif grid[j][i] == grid[j-1][i]:
            happy_cnt += 1
    max_happy_cnt = max(max_happy_cnt, happy_cnt)
    if max_happy_cnt >= m:
        cnt += 1

print(cnt)

