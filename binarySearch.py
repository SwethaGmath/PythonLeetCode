
def binary_search(alist,num):
    begin = 0
    end = len(alist)
    while ( begin <= end ): #for i in range (begin, end):
        mid = (begin + end)//2 
        if (num == alist[mid]):
            return mid
        elif (num > alist[mid]):
            begin = mid+1
        else:
            end = mid -1
    print("number not found in sorted list")

alist=[10,54,8,3,789,45,999]
print("Pleasse enter number")
num = int(input())
alist.sort()
print(alist)

found = binary_search(alist,num)
print("number is found at", found)


    

