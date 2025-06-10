### Check for palindrome

# s = "abcdcba"
# n = len(s)
# mid = int(n / 2)
# # print(int(n/2))
# # print(n/2)
# # print(n//2)

# ############# Using slicing and negative indexing
# fisrtHalf = s[0:mid]
# secondHalf = s[mid:]
# if(n % 2 != 0):
#     secondHalf = s[(mid+1):]
# print(fisrtHalf,secondHalf)
# if(fisrtHalf == secondHalf):
#     print("symmetrical")
# if(fisrtHalf == secondHalf[::-1]):
#     print("palindrome")

######### Using iterative method    
# if(sub == secondHalf[::-1]):
#     print("palindrome")
# print(sub, secondHalf)

# for i in range(n//2):
#     if(s[i] == s[n-i-1]):
#         continue
#     else:
#         print("not palindorme")
#         exit
# print("palindrome")


str = " geeks quiz practice code"
words = str.split(" ")
#print(words)

revWords = list()
### Using list.pop method to get words out in reverse order
for i in range(len(words)):
    revWords.append(words.pop())

print(" ".join(revWords))

####### This wont work after words are popped from the list. The list gets empty
##print(" ".join(reversed(words)))

# revWords = words[::-1]
# print(revWords)
# newStr = " ".join(revWords)
# print(newStr)

######## Longest substring without repeating chars



######## How to Remove Letters From a String in Python
# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks



def removeSubstring(s,sub):
    news = s.replace(sub,"",2) #giving 2 as third arg does not work. but 1 will replace only the first occurance of the substring with blank
    
    print(s,news)
    
    news = "".join([s[i] for i in range(len(s)) if i != 2])
    print (news)
    words = s.split(" ")
    if 's' in words:
        print("yes")
    print(words)

removeSubstring("Geeks123For123Geeks","123")    

