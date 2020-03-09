class User:
    name = "Unknown"
    age = 0
    def setName (self, name):
        self.name = name
    def getName (self):
        return self.name
    def setAge (self, age):
        self.age = age
    def getAge (self):
        return self.age
class Worker (User):
    salary = 0
    def setSalary  (self, salary):
        self.salary=salary
    def getSalary (self):
        return self.salary

John = Worker()
John.setName("John")
John.setAge(25)
John.setSalary(1000)
Jack = Worker()
Jack.setName("Jack")
Jack.setAge(26)
Jack.setSalary(2000)
SumSalary = Jack.getSalary() + John.getSalary()
print (SumSalary)
