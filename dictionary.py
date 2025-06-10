
d1 = {"Name": "Swetha", "Age": 36, 1:"NZ"}
d2 = dict()
d2 = d1
d3 = dict(d2)

for key in d2.keys():
    print(key, "-->",d3.get(key))

 

del d1["Name"]
for k,val in d1.items():
    print(k, "-.",val)


atuple = (1,2,4,5,6)
alist = [1,2,24,2]
t = ()
print (len(atuple))
print(atuple)

