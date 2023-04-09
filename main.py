class Employee:
    increment=1.5
    no_of_employees=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employees+=1
    
    def increase(self):
        self.salary=int(self.salary*Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod
    def isopen(day):
        if day=="Sunday":
            return False
        else: 
            return True

class Programmer(Employee):
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,salary,proglang)
        self.proglang = proglang
        self.exp = exp

a=Programmer("shrey","rohan",99000,'python','5 yrs')
print(a.fname)
print(a.exp)
print(help(Programmer))

print(Employee.no_of_employees)
shrey=Employee('shrey','soral',44000)
rohan=Employee('rohan','das',3000)
Employee.change_increment(4)
shrey.increase()
rohan.increase()
print(shrey.salary)
print(shrey.fname)
print(rohan.salary)
print(Employee.isopen("Sunday"))
# print(shrey.salary)
# print(shrey.fname,rohan.fname)