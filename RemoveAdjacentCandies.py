s="abcddeffgh"

def removeAdjancentCandies(s):
    if s=="":
        return s
    new_string = s
    while(new_string):
        n = len(new_string)
        print("new string is", new_string)
        if(len(new_string) == 2):
            if(new_string[0] == new_string[1]):
                return ""
            else:
                return new_string
        candiesRemoved = False
        for i in range(n-2):            
            if(new_string[i] == new_string[i+1]):
                candiesRemoved = True
                substring=new_string[i]+new_string[i+1]
                print("substring is",substring)
                news = new_string.replace(substring,"")
                print("after string replace", news)
                new_string = news
                break
        if(candiesRemoved == False):
            return new_string

res = removeAdjancentCandies(s)
print("string with no adjacent candies:", res)
