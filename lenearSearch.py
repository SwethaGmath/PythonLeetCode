def lenear_search(alist,num):
    for x in alist:
        if(x == num):
            return alist.index(x)
    print("number not found")

a = [1.23,5,36,50,57,8]
ans = lenear_search(a,50)
print(ans)