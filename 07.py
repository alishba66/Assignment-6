class Employee():
    def __init__ (self, name, salery, ssn):
        self.name = name
        self._salery = salery
        self.__ssn= ssn
     
emp1 = Employee("Ali",50000, "123-456-890")  
print(emp1.name)    
print(emp1._salery)
# print(emp1.__ssn)  
print(emp1._Employee__ssn)