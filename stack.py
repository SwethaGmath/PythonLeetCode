class Stack:
    def __init__(self):
        self._arr=[]
    def push(self,data):
        self._arr.append(data)
    def is_empyt(self):
        if len(self._arr) == 0:
            return True
    def pop(self):
        if(self.is_empyt()):
            print("Stack is empty. Nothing to pop")
            return
        else:
            return self._arr[-1]
    
def reverse_fiile(filename):
    stack = Stack()
    f = open(filename)
    for line in f:
        stack.push(line.rstrip)
    
    f.close()

    outputFile = open("new.txt", "+w")
    while stack.is_empyt() != True:
        outputFile.write(stack.pop+"\n")

    outputFile.close()


### Capitalize first letter of each word

with open("file.txt", "r") as input:
    with open("output.txt","w") as output:
        for i in input:
            arr=i.split(" ")
            for i in arr:
                output.write(i.capitalize())

    