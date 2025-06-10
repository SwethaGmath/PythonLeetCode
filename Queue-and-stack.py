from collections import deque
stack = deque(["abc","ram","john"])
stack.append("iqbal")
print(stack)
stack.pop()
print(stack)

# implement Queue using deque
my = deque(["1","2","3"])
my.append("4")
print(my)
my.appendleft("5")
print(my)
my.append(6)
print(my)
print(my.popleft())


class stack:
    def __init__(self):
        self.stack=[]
    def append(self,val):
        self.stack.append(val)
    def pop(self):
        if not self.stack.is_empty():
            return self.stack.pop[0]
        else:
            return "stack is empty"
    def size(self):
            return len(self.stack)
    def is_empty(self):
         return len(self.stack) == 0