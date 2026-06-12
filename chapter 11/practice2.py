# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'.
# Add a method 'bark' to class 'Dog'.

class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):

    @staticmethod
    def bark():
        print("bow bow")

a=dog()
a.bark()