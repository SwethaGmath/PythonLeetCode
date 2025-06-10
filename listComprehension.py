l = [i for i in range(10)]
def square(n):
    return n*n

resul = [map(square, range(5))]
res2 = [square(i) for i in range(5)]
res3 = map(lambda x: x*x, range(5))

# print even numbers from 1 to 100
evenNum = [n for n in range(100) if n%2 == 0]
print(evenNum)

# printing numbers using lambda 
allNum = map(lambda x: x+2, range(10))
print(list(allNum))

#print(resul, res2, res3)

cities = []
temp = {city:[ i for i in range(7)] for city in cities}

ll = [1,3,34,6,8,9,0,2]
ss = set()
ss.add(4)
ss.add(5)
ss.discard(4)
ss.pop()
print(ss)
if 2 in ll:
    print("yes")
else:
    print("NO")