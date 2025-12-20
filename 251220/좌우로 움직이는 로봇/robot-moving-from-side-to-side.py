n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

'''
한 번 겹치는 것은 카운트, 그때 불린으로 True
이후에 겹치지만 True이면 카운트 X
'''

t, d, t_b, d_b = t[::-1], d[::-1], t_b[::-1], d_b[::-1]
cur_pos_a = cur_pos_b = 0
prev_met = False
met_cnt = 0
timestamp = 0

while t or d or t_b or d_b:
    # A 이동 처리
    if t:
        if d[-1] == 'L':
            cur_pos_a -= 1
        else:
            cur_pos_a += 1
        
        t[-1] -= 1
        if t[-1] == 0:
            t.pop()
            d.pop()
    # B 이동 처리
    if t_b:
        if d_b[-1] == 'L':
            cur_pos_b -= 1
        else:
            cur_pos_b += 1
        
        t_b[-1] -= 1
        if t_b[-1] == 0:
            t_b.pop()
            d_b.pop()
    
    if cur_pos_a == cur_pos_b:
        if not prev_met:
            met_cnt += 1
            prev_met = True
    elif cur_pos_a != cur_pos_b and prev_met:
        prev_met = False

    # timestamp += 1
    # print(cur_pos_a, cur_pos_b, timestamp)
    

print(met_cnt)
