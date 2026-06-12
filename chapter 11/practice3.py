# Create a class 'Employee' and add salary and increment properties to it.

# Write a method 'salaryAfterIncrement' with a @property decorator.

# Create a setter that changes the value of increment based on the salary.

class Employee:
    salary=234
    increment=20
    

    @property
    def SalaryAfterIncement(self):
        return (self.salary+self.salary*0.1)
    
    @SalaryAfterIncement.setter
    def SalaryAfterIncement(self,salary):
        self.increment=((salary/self.salary)-1)*100
    
a=Employee()
print(a.increment)




