import logging
logging.basicConfig(filename=)
def halvesAreAlike(s):
        n = len(s)
        firstHalf = s[:(n//2)]
        firstHalf.lower()
        secondHalf = s[n//2:]
        secondHalf.lower()
        print(firstHalf,secondHalf)
        vowelList=['a','e','i','o','u']
        firstCounter = 0
        secondCounter = 0
        for i in firstHalf:
              if i in vowelList:
                    firstCounter +=1
        for i in secondHalf:
              if i in vowelList:
                    secondCounter +=1
        if(firstCounter == secondCounter):
            return True
        else:
              return False
        

print(halvesAreAlike("textbook"))


def addTwoNumbersFromLinkedList()