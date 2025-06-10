def insertion(arr):
    n = len(arr)
    if(n==0 or n==1):
        return arr
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    return arr
print("sorted array is:", insertion([3,6,12,8,0]))
