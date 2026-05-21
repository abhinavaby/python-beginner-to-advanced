#1. Write a program to print multiplication table of a given number using for loop.
w=int(input("enter the number: "))
for i in range(1,11):
    print(f"{i} * {w} = {i*w}")
