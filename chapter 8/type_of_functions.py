# ==========================================
# 1. BUILT-IN FUNCTIONS
# ==========================================
# print() and len() are built into Python.
# You can use them immediately.

numbers = [10, 20, 30]

length = len(numbers)  # Built-in function to count items
print(f"List length: {length}")  # Built-in function to display output


# ==========================================
# 2. USER-DEFINED FUNCTIONS
# ==========================================
# square_number() is custom-made by the programmer.
# It must be defined before it can be used.


def square_number(num):
    """This is a user-defined function that squares a number."""
    result = num * num
    return result


# Calling the user-defined function
my_square = square_number(5)
print(f"Square of 5 is: {my_square}")
