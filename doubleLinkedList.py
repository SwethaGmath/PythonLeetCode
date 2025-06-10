class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dLinkedList:
    def __init__(self):
        self.head = None
    def insertAtBegin(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node