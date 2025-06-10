from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
stack.appendleft(30)
stack.appendleft(50)
stack.pop()
stack.popleft()

print(stack)