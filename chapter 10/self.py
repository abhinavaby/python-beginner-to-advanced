class employe: #act as template
    
    language = "py" #class attributes
    salary=123333 #class attributes

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")#dunder method which is automatically called when an object is created


    def enter(self):
        print(f"the language={self.language} and salary={self.salary}")


    @staticmethod
    def greet():#doesnot need to give the object inside as it doesnot need any attributs so we use saticmethod decorater,.(it doesnt use object property)
        print("good morning")



# harry=employe()
# harry.language="js"#this is an instence attribute
# print(harry.language,harry.salary)
# harry.enter() #actually going employe.enter(harry)
# harry.greet()

# print()

# abhinav=employe()
# abhinav.greet()
# print(abhinav.salary)

print()


john=employe("rohan",12000,"js")
print(john.name,john.salary,john.language)
