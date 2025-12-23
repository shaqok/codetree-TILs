N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # push_front
    def push_front(self, new_node):
        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    # push_back
    def push_back(self, new_node):
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
    
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    # pop_front
    def pop_front(self):
        popped_val = self.head.data

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

        self.size -= 1
        print(popped_val)

    # pop_back
    def pop_back(self):
        popped_val = self.tail.data

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        self.size -= 1
        print(popped_val)

    # size
    def print_size(self):
        print(self.size)

    # empty
    def empty(self):
        is_empty = 1 if self.size == 0 else 0
        print(is_empty)

    # front
    def front(self):
        print(self.head.data)

    # back
    def back(self):
        print(self.tail.data)

dll = DLL()

for i, comm in enumerate(command):
    if comm == "push_front":
        dll.push_front(Node(A[i]))
    elif comm == "push_back":
        dll.push_back(Node(A[i]))
    elif comm == "pop_front":
        dll.pop_front()
    elif comm == "pop_back":
        dll.pop_back()
    elif comm == "front":
        dll.front()
    elif comm == "back":
        dll.back()
    elif comm == "size":
        dll.print_size()
    elif comm == "empty":
        dll.empty()
