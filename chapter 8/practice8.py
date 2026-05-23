#8. Write a python function to print multiplication table of a given number.
def mult(n):
    for i in range(1,11):
        print(f"{i} * {n} = {i*n}")

w=int(input("enter the number: "))
mult(w)
