myList = [10, 5,3,1,7,9,90]

myList.append(99)
print(myList.pop())
print(sum(myList))
myListTostr = [str(i) for i in myList]
s = "->".join(myListTostr)
print(s)
print(sorted(myList))
print(myList)

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
newData = sorted(student_tuples, key = lambda student: student[2], reverse = True)
print(newData)
