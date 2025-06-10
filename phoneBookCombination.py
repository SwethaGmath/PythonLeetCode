d = {'2':'abc','3':'def','4':'ghi','5':'jkl'}
def fun(input):
    inputStr = str(input)
    n = len(str(inputStr))
    if(n == 0):
        return []
    if(n==1):
        return list(d[inputStr[0]])
    ff = [x+y for x in list(d[inputStr[0]]) for y in list(d[inputStr[1]])]
    if(n == 2):
        return ff
    if(n ==3):
        gg = [x+y for x in ff for y in list(d[inputStr[2]])]
    
print(fun(4))
