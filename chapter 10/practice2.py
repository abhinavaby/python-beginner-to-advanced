# Write a class "Calculator" capable of finding square, cube and square root
# of a number.

class calculator:
    def __init__(self,num):
        self.num=num
    
    def cal(self):
        print(f"square:{self.num**2}\ncube:{self.num**3}\nsquare root:{self.num**0.5}")
c=calculator(4)
c.cal()