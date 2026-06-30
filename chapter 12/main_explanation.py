def myFunc():
    # Function Definition:
    # This function prints "Hello world!" when it is called.
    print("Hello world!")


# Function Call:
# Executes the code inside the function.
myFunc()


# __name__ is a special built-in variable in Python.
# It tells us whether the file is being run directly
# or imported as a module.

print(__name__)


"""
Explanation
===========

1. def myFunc():
   - Defines a function named 'myFunc'.
   - The function is stored in memory.
   - It does NOT execute at this point.

2. myFunc()
   - Calls the function.
   - Python enters the function body.
   - Executes:
         print("Hello world!")

3. print(__name__)
   - Prints the value of the special variable '__name__'.

   If this file is executed directly:
       __name__ = "__main__"

   Example:
       python main.py

       Output:
       Hello world!
       __main__

   If this file is imported into another Python file:

       import main

       Then:
       __name__ = "main"

       Output:
       Hello world!
       main

4. Why is __name__ useful?

   It is commonly used with:

       if __name__ == "__main__":
           myFunc()

   This ensures that the function runs ONLY when the file
   is executed directly, and NOT when it is imported as a module.

Execution Flow
==============

Program Starts
      │
      ▼
Function Definition (No execution)
      │
      ▼
myFunc() is called
      │
      ▼
Prints:
Hello world!
      │
      ▼
print(__name__)
      │
      ▼
Prints:
__main__   (if run directly)
or
module_name (if imported)
      │
      ▼
Program Ends

Expected Output (Run Directly)
==============================

Hello world!
__main__
"""