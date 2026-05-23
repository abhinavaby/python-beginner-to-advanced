# sum on n natural numbers
def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
w=int(input("enter the number to find the sum of n numbers: "))
q=sum(w)
print(f"the sum of first {w} namural numbers is {q}")