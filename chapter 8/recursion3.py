def sum(n):
    if(n==0):
        return 0
    else:
        return n%10+sum(n//10)
    
w=int(input("enter the number to find sum of digits: "))
q=sum(w)
print(f"the sum of digits of the number {w} is {q}")