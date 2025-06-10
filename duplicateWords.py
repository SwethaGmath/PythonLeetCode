a = "the is best dog is the best the"
new_a = a.split(' ')
print(new_a)
new_a.sort()
print(new_a)
dup = []
for i in range(len(new_a)-1):
    if(new_a[i] == new_a[i+1]):
        dup.append(new_a[i])
        
print("repated set of words is", list(set(dup)))