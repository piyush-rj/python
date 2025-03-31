class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def getSalary(self):
        print(self.salary)


piyush = Employee("Piyush Raj", "100,000")
print(piyush.name)
print(piyush.salary)

piyush.getSalary()