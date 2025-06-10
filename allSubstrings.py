str = "abcd"
print(str[0:0+1])
def allSubstring(s):
    substrings=[]
    n = len(s)
    for i in range(1,n):
        for j in range(0,n):
            substrings.append(s[:j+i])
            #print(substrings)
    print(substrings)

allSubstring(str)