#4. Write a program to find whether a given number is prime or not.
w=int(input("enter the number: "))
c=0
for i in range(1,w+1):
    if(w%i==0):
        c+=1
if(c==2):
    print(f"{w} is a prime number")
else:
    print(f"its not a prime number")