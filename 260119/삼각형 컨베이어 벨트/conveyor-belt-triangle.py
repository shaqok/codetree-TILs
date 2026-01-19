from collections import deque

n, t = map(int, input().split())

l = list(map(str, input().split()))
r = list(map(str, input().split()))
d = list(map(str, input().split()))

# Please write your code here.
l_q = deque(l)
r_q = deque(r)
d_q = deque(d[::-1])

for _ in range(t):
    r_q.appendleft(l_q.pop())
    d_q.append(r_q.pop())
    l_q.appendleft(d_q.popleft())

print(" ".join(l_q))
print(" ".join(r_q))
print(" ".join(list(d_q)[::-1]))