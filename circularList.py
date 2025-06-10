class Node:
    def __init__(self,data):
        self.data = data
        self.next = self

class cLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            current = self.head
            while(current.next != self.head):
                current= current.next
            current.next = node
            node.next = self.head
            self.head = node

    def Display(self):
         current = self.head
         print(current.data, end=" ")
         while(current.next != self.head):
             current = current.next
             print("-->",current.data, end=" ")
         print("-->",current.next.data)

        
             


cList = cLinkedList()
cList.insert(10)
cList.insert(20)
cList.insert(30)
cList.Display()

