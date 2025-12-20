N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

'''
set을 활용해서 이전 조합과 값이 달라지는지 확인
총 순회 range는 total_t = sum(t)
'''

switch_cnt = 0

v, t = v[::-1], t[::-1]
v2, t2 = v2[::-1], t2[::-1]
total_t = sum(t)

cur_pos_a = cur_pos_b = 0
first_rank = set()

for i in range(total_t):
    cur_v_a, cur_v_b = v[-1], v2[-1]
    cur_t_a, cur_t_b = t[-1], t2[-1] 

    if v:
        cur_pos_a += cur_v_a
        t[-1] -= 1
        if t[-1] == 0:
            t.pop()
            v.pop()

    if v2:
        cur_pos_b += cur_v_b
        t2[-1] -= 1
        if t2[-1] == 0:
            t2.pop()
            v2.pop()

    # 랭킹 시스템
    if cur_pos_a == cur_pos_b:
        cur_rank = set(['A', 'B'])
    elif cur_pos_a > cur_pos_b:
        cur_rank = set(['A'])
    else:
        cur_rank = set(['B'])

    if first_rank != cur_rank:
        first_rank = cur_rank
        switch_cnt += 1

    # print(i, cur_pos_a, cur_pos_b, cur_rank, first_rank, switch_cnt)

print(switch_cnt)

