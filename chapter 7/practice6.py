#6. Write a program to calculate the factorial of a given number using for loop.
w=int(input("enter the number: "))
fact=1
for i in range(1,w+1):
    fact*=i
print(f"the factorial of {w} is {fact}")