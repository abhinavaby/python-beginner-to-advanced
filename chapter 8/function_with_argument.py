def greet(name,end):
    print(f"hello {name} , {end}")

greet("abhinav","hi") # here abhinav,hi are the parameter
greet("Rohan","hello") # here Rohan,hello are the parameter
print()
print()

# ==========================================
# 1. PARAMETERS (The Placeholders)
# ==========================================
# 'name' and 'age' are parameters.
# They are variables defined inside the parentheses.


def greet_person(name, age):
    print(f"Hello {name}, you are {age} years old.")


# ==========================================
# 2. ARGUMENTS (The Real Values)
# ==========================================
# "Alice" and 25 are arguments.
# They are the actual data sent to the function.

greet_person("Alice", 25)

# "Bob" and 30 are a different set of arguments.
greet_person("Bob", 30)
