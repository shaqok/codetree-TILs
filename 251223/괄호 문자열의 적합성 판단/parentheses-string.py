str = input()

# Please write your code here.

stack = []
is_error = False
for s in str:
    if s == '(':
        stack.append(s)
    elif len(stack) == 0:
        is_error = True
        break
    else:
        stack.pop()

if is_error or stack:
    print('No')
else:
    print('Yes')