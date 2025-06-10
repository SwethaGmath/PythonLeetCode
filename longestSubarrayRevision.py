def longestSubarray(a, k):
    n = len(a)
    longestLength = 0
    longestSubarray = list()
    for i in range(n):
        sum = 0
        sublist = list()
        for j in range(i,n):
            sum += a[j]
            if(sum <= k):
                sublist.append(a[j])
                longestLength = max(longestLength, j-i+1)
                if(len(sublist) > len(longestSubarray)):
                    longestSubarray = sublist
        
    return (longestSubarray,longestLength)

print(longestSubarray([14,5,9,2,6,1,2,1], 10))


