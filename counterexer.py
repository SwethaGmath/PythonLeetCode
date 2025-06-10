from collections import Counter

a = [1,3,5,8,2,1,5,8,43]
c = Counter(a)
for k,v in c.items():
    print(k,v)
