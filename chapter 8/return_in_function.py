# ==========================================
# 1. DEFINING THE RETURN VALUE
# ==========================================
def calculate_tax(price):
    tax_amount = price * 0.15  # Calculate 15% tax
    return tax_amount  # Send the result back out
    print("This line will never run")  # Code after 'return' is ignored


# ==========================================
# 2. CAPTURING AND USING THE RETURN VALUE
# ==========================================
# The function runs, and the value (15.0) replaces the function call.
my_tax = calculate_tax(100)

# Now 'my_tax' holds the value 15.0 and can be used elsewhere.
final_bill = 100 + my_tax
print(f"Total Bill: ${final_bill}")


# ==========================================
# 3. FUNCTIONS WITHOUT A RETURN VALUE
# ==========================================
def say_hello():
    return ("Hello!")  # Prints to screen, but does not 'return' data


result = say_hello()
print(f"Captured value: {result}")  # Prints 'None' because nothing was returned
