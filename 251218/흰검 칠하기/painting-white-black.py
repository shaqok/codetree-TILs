n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
k = n * max(x)

# color: 0 - None, 1 - Black, 2 - White, 3 - Grey
arr = [(0, 0, 0)] * (2 * (k + 1))

cur_pos = k // 2

for cur_move, cur_dir in zip(x, dir):
    if cur_dir == 'R':
        for i in range(cur_pos, cur_pos + cur_move):
            cur_color, cur_black_cnt, cur_white_cnt = arr[i]
            cur_black_cnt += 1

            arr[i] = (1, cur_black_cnt, cur_white_cnt)

            # check grey
            if cur_black_cnt >= 2 and cur_white_cnt >= 2:
                arr[i] = (3, cur_black_cnt, cur_white_cnt)
            else:
                arr[i] = (1, cur_black_cnt, cur_white_cnt)
        
        cur_pos = cur_pos + cur_move - 1
    else:
        for i in range(cur_pos, cur_pos - cur_move, -1):
            cur_color, cur_black_cnt, cur_white_cnt = arr[i]
            cur_white_cnt += 1

            # check grey
            if cur_black_cnt >= 2 and cur_white_cnt >= 2:
                arr[i] = (3, cur_black_cnt, cur_white_cnt)
            else:
                arr[i] = (2, cur_black_cnt, cur_white_cnt)

        cur_pos = cur_pos - cur_move + 1

arr = [tile for tile in arr if tile[0] != 0]
black_cnt = len([tile for tile in arr if tile[0] == 1])
white_cnt = len([tile for tile in arr if tile[0] == 2])
grey_cnt = len([tile for tile in arr if tile[0] == 3])

print(white_cnt, black_cnt, grey_cnt)

