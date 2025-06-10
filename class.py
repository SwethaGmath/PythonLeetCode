class Person:
    Name = ""
    Age = 0
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def display(self):
        print(self.Name, self.Age)

class Employee(Person):
    Role = ""
    def __init__(self,age,name,role):
        self.Age = age
        self.Name = name
        self.Role = role
    def display(self):
        print(self.Role,self.Age, self.Name)


    
emp = Employee(30,"swetha", "Engineer")
emp.display()
#print(emp.Age, emp.Name)
#print("Employee details are {} {}".format(emp.Age, emp.Name))
