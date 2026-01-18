from collections import deque

n, t = map(int, input().split())
u = list(map(str, input().split()))
d = list(map(str, input().split()))[::-1]

# Please write your code here.
"""
t초의 루프에서
    u의 끝의 값을 빼고
    d에 넣는다
    d의 앞의 값을 빼고
    u의 앞에 넣는다
"""
u_deque = deque(u)
d_deque = deque(d)

for _ in range(t):
    u_last = u_deque.pop()
    d_deque.append(u_last)
    d_first = d_deque.popleft()
    u_deque.appendleft(d_first)

print(" ".join(u_deque))
print(" ".join(list(d_deque)[::-1]))