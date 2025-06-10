def maxProduct(a):
    new_a = sorted(a)
    print (a)
    a.sort()
    print(a)
    res = (new_a[-1] * new_a[-2])
    rev_a = a[::-1]
    print("reversed array with indexing", rev_a)
    n = len(a)
    b=[]
    for i in range(n-1, -1, -1):
        b.append(a[i])
    print( "reversed array with looping indexing", b)

    return res

print(maxProduct([3,1,56,8,9]))

