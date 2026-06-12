 # Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twodVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i}i + {self.j}j")

class threedVector(twodVector):
    
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
        
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

a=twodVector(1,2)
b=threedVector(1,2,3)
a.show()
b.show()
