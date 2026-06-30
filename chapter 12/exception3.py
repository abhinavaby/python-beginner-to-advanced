try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except TypeError:
    print("Error: Invalid data type.")

except:
    print("An unexpected error occurred.")

finally:
    print("Program execution completed.")