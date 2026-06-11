"""
==========================
INHERITANCE IN PYTHON
==========================

Inheritance allows a class (Child/Derived Class) to acquire
properties and methods of another class (Parent/Base Class).

Advantages:
1. Code Reusability
2. Extensibility
3. Maintainability
4. Supports Polymorphism
"""

# =====================================================
# 1. SINGLE INHERITANCE
# =====================================================

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()     # inherited method
d.bark()


print("\n" + "="*50)

# =====================================================
# 2. MULTILEVEL INHERITANCE
# =====================================================

class GrandParent:
    def grandparent_method(self):
        print("Grandparent Method")

class Parent(GrandParent):
    def parent_method(self):
        print("Parent Method")

class Child(Parent):
    def child_method(self):
        print("Child Method")

c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()


print("\n" + "="*50)

# =====================================================
# 3. MULTIPLE INHERITANCE
# =====================================================

class Father:
    def father_skill(self):
        print("Driving")

class Mother:
    def mother_skill(self):
        print("Cooking")

class Son(Father, Mother):
    pass

s = Son()
s.father_skill()
s.mother_skill()


print("\n" + "="*50)

# =====================================================
# 4. HIERARCHICAL INHERITANCE
# =====================================================

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car()
bike = Bike()

car.start()
bike.start()


print("\n" + "="*50)

# =====================================================
# 5. HYBRID INHERITANCE
# =====================================================

class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()


print("\n" + "="*50)

# =====================================================
# super() FUNCTION
# =====================================================

class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor Called")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # call parent constructor
        self.roll = roll
        print("Student Constructor Called")

stu = Student("Abhinav", 101)
print(stu.name, stu.roll)


print("\n" + "="*50)

# =====================================================
# METHOD OVERRIDING
# =====================================================

class Bird:
    def sound(self):
        print("Bird makes sound")

class Parrot(Bird):
    def sound(self):   # overriding parent method
        print("Parrot says Hello")

p = Parrot()
p.sound()


print("\n" + "="*50)

# =====================================================
# CLASS ATTRIBUTE IN INHERITANCE
# =====================================================

class Employee:
    company = "Microsoft"

class Programmer(Employee):
    language = "Python"

emp = Programmer()

print(emp.company)   # inherited attribute
print(emp.language)


print("\n" + "="*50)

# =====================================================
# isinstance() and issubclass()
# =====================================================

class Parent:
    pass

class Child(Parent):
    pass

obj = Child()

print(isinstance(obj, Child))    # True
print(isinstance(obj, Parent))   # True

print(issubclass(Child, Parent)) # True


print("\n" + "="*50)

# =====================================================
# METHOD RESOLUTION ORDER (MRO)
# =====================================================

class X:
    def show(self):
        print("Class X")

class Y(X):
    pass

class Z(X):
    pass

class Test(Y, Z):
    pass

t = Test()
t.show()

print(Test.mro())  # order Python searches classes


print("\n" + "="*50)

# =====================================================
# ACCESSING PARENT METHOD EXPLICITLY
# =====================================================

class Parent:
    def display(self):
        print("Parent Display")

class Child(Parent):
    def display(self):
        print("Child Display")

        # Call Parent Method
        Parent.display(self)

c = Child()
c.display()


print("\n" + "="*50)

# =====================================================
# SUMMARY
# =====================================================

"""
Types of Inheritance:

1. Single Inheritance
   A -> B

2. Multilevel Inheritance
   A -> B -> C

3. Multiple Inheritance
   A
    \
     C
    /
   B

4. Hierarchical Inheritance
      A
     / \
    B   C

5. Hybrid Inheritance
   Combination of multiple inheritance types.

Important Concepts:
✓ super()
✓ Method Overriding
✓ MRO (Method Resolution Order)
✓ isinstance()
✓ issubclass()

"""