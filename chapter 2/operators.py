"""operators in python
    ------------------
    arithamatic:+,-,*,/ etc
    assignment:=,+=,-=, etc
    comparison:==,>,>=,<.!= etc
    logical:and,or,not
    """

# Arithamatic operators

a=10
b=3
w=a+b
print(f"the sum of {a} and {b} is {w}")
print()

# Assignment Operator

a=5+3 # Assigning the vale of 5+3 to variable a 
a+=3 # Increment the value of a by three
print(f"the value of a = {a}")
print()

# Comparison operators

q=10
w=3
print(q>w) # Returns True or False
print(q==w) # Returns True or False
print(q<w) # Returns True or False
print(q!=w) # Returns True or False
print()


# Logical Operator
e = True or False
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

print()

# Truth Table for AND (and)
# Returns True only if both inputs are True.
print("--- AND Truth Table ---")
print(f"True and True   -> {True and True}")
print(f"True and False  -> {True and False}")
print(f"False and True  -> {False and True}")
print(f"False and False -> {False and False}\n")

print()
# Truth Table for NOT (not)
# Inverts the Boolean input value.
print("--- NOT Truth Table ---")
print(f"not True  -> {not True}")
print(f"not False -> {not False}")


