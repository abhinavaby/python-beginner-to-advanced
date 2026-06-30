def main():
    try:
        # Code that may raise an exception
        a = int(input("Hey, Enter a number: "))
        print(f"You entered: {a}")

        # return exits the function,
        # but the finally block will still execute.
        return

    except Exception as e:
        # Executes only if an exception occurs
        print("Exception caught:", e)

        # Even after this return,
        # the finally block will still execute.
        return

    finally:
        # This block ALWAYS executes, regardless of:
        # 1. Whether an exception occurred
        # 2. Whether a return statement was executed
        # 3. Whether the try block completed successfully
        print("Hey I am inside of finally")


# Call the function
main()

"""
Example 1 (Valid Input)
-----------------------
Input:
Hey, Enter a number: 25

Output:
You entered: 25
Hey I am inside of finally


Example 2 (Invalid Input)
-------------------------
Input:
Hey, Enter a number: abc

Output:
Exception caught: invalid literal for int() with base 10: 'abc'
Hey I am inside of finally


Execution Flow
--------------
Valid Input:
main()
   │
   ▼
try
   │
   ▼
print(a)
   │
   ▼
return
   │
   ▼
finally
   │
   ▼
Function exits

Invalid Input:
main()
   │
   ▼
try
   │
   ▼
Exception
   │
   ▼
except
   │
   ▼
return
   │
   ▼
finally
   │
   ▼
Function exits

Key Point:
-----------
The 'finally' block ALWAYS executes before the function actually exits,
even if a 'return' statement is encountered inside the try or except block.
"""