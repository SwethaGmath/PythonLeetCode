
def checkBalanced(s):
    paranthList=[]
    for i in s:
        if i=='(' or i =='{' or i =='[':
            paranthList.append(i)
        if i==')':
            if(paranthList[-1] == '('):
                paranthList.pop()
            else:
                return False
        if i =='}':
            if(paranthList[-1] == '{'):
                paranthList.pop()
            else:
                return False
        if i == ']':
            if(paranthList[-1] == '['):
                paranthList.pop()
            else:
                return False

    if len(paranthList) == 0:
        return True
    else:
        return False

print(checkBalanced("[]()"))
