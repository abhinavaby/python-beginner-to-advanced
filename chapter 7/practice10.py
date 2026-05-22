#10. Write a program to print multiplication table of n using for loops in reversed order.
w=int(input("enter the number: "))
for i in range(10,1):
    print(f"{i} * {w} = {i*w}")