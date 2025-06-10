def majorityElement(arr):
        #Your code here
        majority=arr[0]
        n = len(arr)
        majority = -1
        
        for i in range(0, n-1):
            count = 1
            for  j in range(i+1, n-1):
                if(arr[i] == arr[j]):
                    count+=1 
            if ( count >= (n/2)):
                majority = arr[i]
        return majority

print(majorityElement([5]))

