# Python class to handle comments

#store the comments

# 1. Add a comment
# 2. Get all comments

#linear linked list

class Node:
    def __init__(self,data, userNAme,userId, timestamp):
        self.data= data
        self.UserData = userNAme
        self.UserData = userId
        self.UserData = timestamp
        self.commentId = None
        self.replies = None
        self.next = None


class Comment:
    def __init__(self):
        self.head = None
        self.commentCounter = 0
    
    def addComment(self,data,userNAme,userId, timestamp):  # /add
        newNode = Node(data,userNAme,userId, timestamp)
        newNode.commentId = self.commentCounter + 1
        if(self.head == None):
            self.head = newNode           
        else:
            newNode.next = self.head
            self.head= newNode
   
        
    def getComments(self):  # /get
        if(self.head == None):
            print("There are no comments to show")
            return
        else:
            stringArra = []
            current = self.head
            while(current != None):
                #print(current.data)
                stringArra.append(current.data)
                current= current.next
            return stringArra
        
    def replyToComment(self, comment, commentId):
        self.addComment(comment)
        #newNode = Node(comment)
        # a get function to get to the node with the commentId
       
        if commentId == None:
            return "Comment ID required"
         
        temp = self.head
        
        while temp.commentId != commentId | temp != None:
            temp = temp.next
        if(temp == None):
            return("commentId not found")
        
        temp.replies = newNode
        #return "Success!,"
        return comment.c

   # def addReactionToTheComment(self, reaction, commentId):



comm = Comment()
commentId = comm.addComment("first comment","A","Ids","TimeStamp", "location")
#new guid()

comm.addComment("second comment","B")
comm.addComment("")
comm.replyToComment("reply",commentId)

res = comm.getComments()


#ECR commentService





