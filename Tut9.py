class Employee:
    increment=1.5
    no_of_employees=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.email=fname+lname+"@email.com"
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

if __name__=="__main__":
    shrey=Employee("shrey","jackson",900)
    print(shrey.email)