def numPalindrome(n):
    num = str(n)
    n = len(num)
    i = 0
    j = n-1
    flag = True
    while(i<=j):
        if(num[i] == num[j]):
            i+=1
            j-=1
        else:
            print("number is not palindrome")
            flag = False
            break
    if(flag):
        print("number is palindorme")
numPalindrome(12321)