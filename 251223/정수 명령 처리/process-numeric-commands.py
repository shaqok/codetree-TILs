N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            val = self.stack.pop()
            print(val)
    
    def size(self):
        print(len(self.stack))
    
    def empty(self):
        print(1 if not self.stack else 0)
    
    def top(self):
        print(self.stack[-1])
        
stack = Stack()

for i, comm in enumerate(command):
    if comm == "push":
        stack.push(value[i])
    elif comm == "pop":
        stack.pop()
    elif comm == "size":
        stack.size()
    elif comm == "empty":
        stack.empty()
    elif comm == "top":
        stack.top()

