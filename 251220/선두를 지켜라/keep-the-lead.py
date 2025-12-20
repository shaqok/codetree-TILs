n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

'''
switch_cnt = 0
cur_first_place = None
MAX_TIME = sum(t)

cur_pos_1 = cur_pos_2 = 0
MAX_TIME만큼 순회하며:

'''

switch_cnt = 0
cur_first_place = None
MAX_TIME = sum(t)

cur_pos_1 = cur_pos_2 = 0
player_A, player_B = 'A', 'B'

v, t = v[::-1], t[::-1]
v2, t2 = v2[::-1], t2[::-1]

for i in range(MAX_TIME):
    # A의 이동 계산
    if t:
        cur_pos_1 += v[-1]
        t[-1] -= 1
        if t[-1] == 0:
            t.pop()
            v.pop()
    # B의 이동 계산
    if t2:
        cur_pos_2 += v2[-1]
        t2[-1] -= 1
        if t2[-1] == 0:
            t2.pop()
            v2.pop()
    # 선두 계산
    if i == 0:
        if cur_pos_1 > cur_pos_2:
            cur_first_place = player_A
        elif cur_pos_1 < cur_pos_2:
            cur_first_place = player_B
    elif cur_pos_1 > cur_pos_2 and cur_first_place != player_A:
        cur_first_place = player_A
        switch_cnt += 1 
    elif cur_pos_1 < cur_pos_2 and cur_first_place != player_B:
        cur_first_place = player_B
        switch_cnt += 1

print(switch_cnt)