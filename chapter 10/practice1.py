# Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.

class information:
    company="microsoft"
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language



    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Salary: {self.salary}")
        print(f"Language: {self.language}")
        print()


p1=information("rohan",10000,"python")
p2=information("jacob",1100,"java")

#information

p1.get_info()
p2.get_info()


        