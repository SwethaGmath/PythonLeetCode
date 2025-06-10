def palindrome(x):
    s = str(x)
    rs = s[::-1]
    print(rs)
    print(s)
    if(s[0] =="-"):
        return False
    if(s == rs):
        return True
    else:
        return False
    
# without using reverse function
    if(x < 0 ):
        return False

    temp = x
    rev_num = 0
    while( temp > 0):
        rev_num = rev_num*10 + temp %10
        temp //= 10
    if rev_num == x:
        return True
    else:
        return False


    
print(palindrome(10))