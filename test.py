from collections import deque

stack = deque()

stack.append(7)
stack.append(8)
print(stack.pop())
print(stack[-1])
stack.append(9)
print(len(stack))
