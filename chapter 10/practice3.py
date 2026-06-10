# Create a class with a class attribute a; create an object from it and set
# 'a' directly using object.a = 0. Does this change the class attribute?


class sample:
    a=1

w=sample()
w.a=0

print(f"class value of a={sample.a}\nobject value of a={w.a}")


# Object Attribute: Instance Attribute
# Class Attribute: Class Attribute
# Answer: No, the class attribute does not change because an instance attribute is created for that object.