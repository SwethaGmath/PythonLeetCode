Class Salary:

    def __init__(self, Pay, Bonus):
        self.Pay = Pay
        self.Bonus = Bonus

class Employee:
    def __init__(self,Name,Age, Pay, Bonus):
        self.Name= Name
        self.Age = Age
        self.Salry = Salary(Pay, Bonus)