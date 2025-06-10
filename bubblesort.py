

def bubble_srot(alist):
    swapped = False
    l = len(alist)
    for i in range(l-1):
        for j in range(0, l-i-1):
            if(a[j] > a[j+1]):
                swapped = True
                a[j],a[j+1] = a[j+1],a[j]

        if ( swapped == False):
            exit


a = [10,57,12,6,5347,463,2,1,5,7]
#a.sort()
print(a)

bubble_srot(a)
print(a)