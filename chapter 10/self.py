class employe: #act as template
    
    language = "py" #class attributes
    salary=123333 #class attributes
    def enter(self):
        print(f"the language={self.language} and salary={self.salary}")
    def greet(self):
        print("good morning")



harry=employe()
harry.language="js"#this is an instence attribute
print(harry.language,harry.salary)
harry.enter() #actually going employe.enter(harry)
harry.greet()
