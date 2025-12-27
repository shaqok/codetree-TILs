from collections import deque

n, k = map(int, input().split())

# Please write your code here.
dq = deque()
result = []

for i in range(n):
    dq.append(i+1)

while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    popped = dq.popleft()
    result.append(str(popped))

print(' '.join(result))
