# Average of n numbers
a=int(input("enter the limit: "))
sum=0
for i in range(a):
    
    b=int(input(f"enter the {i+1} number: "))
    sum+=b
avg=sum/a
print(f"avg={avg}")   