def rec(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*rec(n-1)
w=int(input("enter the number to find factorial: "))
q=rec(w)
print(f"the factorial of {w} is {q}")