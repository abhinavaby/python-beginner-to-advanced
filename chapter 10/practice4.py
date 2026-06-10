# Add a static method in problem 2, to greet the user with hello.
class calculator:
    def __init__(self,num):
        self.num=num
    @staticmethod
    def greet():
        print("hello")
    
    def cal(self):
        print(f"square:{self.num**2}\ncube:{self.num**3}\nsquare root:{self.num**0.5}")
c=calculator(4)
c.cal()
c.greet() # calling static method function 