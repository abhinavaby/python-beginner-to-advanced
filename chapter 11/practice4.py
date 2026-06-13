# Write a class 'Complex' to represent complex numbers.

# Overload the '+' operator to add two complex numbers.

# Overload the '*' operator to multiply two complex numbers.

class complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r
        

    def __add__(self, c):
        return complex(self.r + c.r , self.i + c.i)
    
    def __mul__(self, b):
        # formula= (a+bi)(c+di)=(ac−bd)+(ad+bc)i
        return complex((self.r*b.r)-(self.i*b.i),(self.r*b.i)+(self.i*b.r))

    def __str__(self):
        return (f"{self.r} + {self.i}i")
    

a=complex(1,3)
b=complex(3,4)
print(a+b)
print(a*b)