a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if(b==0):
    raise ZeroDivisionError("we can't divide with 0")

else:
    print(f"a / b = {a/b}")
    print("program executed sucessfully")