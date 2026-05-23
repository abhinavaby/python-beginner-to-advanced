# ==========================================
# 1. DEFINING DEFAULT PARAMETERS
# ==========================================
# 'message' has a default value of "Hello".
# 'name' has no default value and is mandatory.


def greet(name, message="Hello"):
    return f"{message}, {name}!"


# ==========================================
# 2. CALLING THE FUNCTION
# ==========================================

# Scenario A: Using the default value
# We only pass the mandatory 'name' argument.
default_call = greet("Alice")
print(default_call)  # Output: Hello, Alice!


# Scenario B: Overriding the default value
# We pass both arguments to replace the default message.
custom_call = greet("Bob", "Good morning")
print(custom_call)  # Output: Good morning, Bob!

print()
