n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

'''
둘 중 더 긴 시간을 총 루프의 시간으로 정한다

각 루프에 둘의 포지션을 체크해서 같다면 멈추기 -> 몇초 지났는지 출력

루프가 끝났다면 -> 만나지 않았다면 -1
'''

k = max(sum(t), sum(t2))

timestamp = 0
is_met = False
cur_pos_1 = cur_pos_2 = 0
d, t = d[::-1], t[::-1]
d2, t2 = d2[::-1], t2[::-1]

while d or t or d2 or t2:
    if timestamp != 0 and cur_pos_1 == cur_pos_2:
        is_met = True
        break

    if t:
        if d[-1] == 'L':
            cur_pos_1 -= 1
        else:
            cur_pos_1 += 1

        t[-1] -= 1
        if t[-1] == 0:
            d.pop()
            t.pop()

    if t2:
        if d2[-1] == 'L':
            cur_pos_2 -= 1
        else:
            cur_pos_2 += 1

        t2[-1] -= 1
        if t2[-1] == 0:
            d2.pop()
            t2.pop()

    timestamp += 1

if is_met:
    print(timestamp)
else:
    print(-1)


