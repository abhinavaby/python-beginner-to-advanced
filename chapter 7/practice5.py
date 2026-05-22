#5. Write a program to find the sum of first n natural numbers using while loop.
w=int(input("enter the limit: "))
i=1
s=0
while(i<=w):
    s+=i
    i+=1
print(f"the sum of first {w} natural number = {s}")