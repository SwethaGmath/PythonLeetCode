class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class sLinkedList:
    def __init__(self):
        self.head = None


    def inertAtBegin(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self):
        if(self.head):
            myList = list()
            current = self.head
            while(current):
                myList.append(current.data)
                current = current.next
            myStrList = [str(i) for i in myList]
            print("-->" .join(myStrList))
        
        
    def insertAtIndex(self,data,pos):
        newNode = Node(data)
        index = 0
        current = self.head
        if(pos == index):
            self.inertAtBegin(data)
        else:
            while(current != None and index+1 != pos):
                current = current.next
                index += 1
            if(current == None):
                print("Given position not found in the linked list")
            else:
                newNode.next = current.next
                current.next = newNode
                
    def display(self):
        

if __name__ == "__main__":
    list1 = sLinkedList()
    list1.inertAtBegin(10)
    list1.insertAtIndex(5,1)
   
    list1.inertAtBegin(20)
    list1.inertAtBegin(30)
    list1.insertAtIndex(25,2)
    list1.insertAtIndex(15,2)

    list1.display()


        

