"""
DECORATORS IN INHERITANCE
========================

Common decorators used with inheritance:
1. @staticmethod
2. @classmethod
3. @property
"""

# =====================================================
# 1. @staticmethod with Inheritance
# =====================================================

class Parent:
    @staticmethod
    def greet():
        print("Hello from Parent")

class Child(Parent):
    pass

Child.greet()      # Inherited static method


print("\n" + "="*50)

# =====================================================
# 2. @classmethod with Inheritance
# =====================================================

class Employee:
    company = "Microsoft"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

class Programmer(Employee):
    pass

print("Before:", Programmer.company)

Programmer.change_company("Google")

print("After :", Programmer.company)
print("Employee Company:", Employee.company)


print("\n" + "="*50)

# =====================================================
# 3. @property with Inheritance
# =====================================================

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

class Student(Person):
    pass

s = Student("Abhinav", "Aby")

print(s.fullname)


print("\n" + "="*50)

# =====================================================
# 4. Overriding Decorated Methods
# =====================================================

class Animal:
    @staticmethod
    def sound():
        print("Animal Sound")

class Dog(Animal):
    @staticmethod
    def sound():
        print("Bark Bark")

Animal.sound()
Dog.sound()


print("\n" + "="*50)

# =====================================================
# 5. @property + Setter in Inheritance
# =====================================================

class Vehicle:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

class Car(Vehicle):
    pass

c = Car(100)

print(c.speed)

c.speed = 120

print(c.speed)


print("\n" + "="*50)

# =====================================================
# 6. Real Example: @classmethod + Inheritance
# =====================================================

class Person:
    country = "India"

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

class Student(Person):
    pass

class Teacher(Person):
    pass

Student.change_country("USA")

print("Student:", Student.country)
print("Teacher:", Teacher.country)
print("Person :", Person.country)


print("\n" + "="*50)

# =====================================================
# SUMMARY
# =====================================================

"""
@staticmethod
--------------
- No self
- No cls
- Acts like a normal function inside a class
- Can be inherited

@classmethod
--------------
- Receives cls (class reference)
- Can modify class attributes
- Works with inheritance

@property
-------
- Access method like an attribute
- Supports getter, setter, deleter
- Can be inherited and overridden

Inheritance + Decorators
-------------------------
Child class inherits decorated methods
and properties from Parent class unless
they are overridden.
"""