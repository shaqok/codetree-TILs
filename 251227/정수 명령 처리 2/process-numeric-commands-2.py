from collections import deque

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, data):
        self.dq.append(data)

    def pop(self):
        if self.dq:
            print(self.dq.popleft())

    def size(self):
        print(len(self.dq))
    
    def empty(self):
        print(1 if len(self.dq) == 0 else 0)
    
    def front(self):
        if self.dq:
            print(self.dq[0])

queue = Queue()

for i, comm in enumerate(command):
    if comm == "push":
        queue.push(A[i])
    elif comm == "pop":
        queue.pop()
    elif comm == "size":
        queue.size()
    elif comm == "empty":
        queue.empty()
    elif comm == "front":
        queue.front()