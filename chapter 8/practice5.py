"""5. Write a python function to print first n lines of the following pattern:
***
**     - for n = 3
*
"""
def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("* ",end=" ")
        print()

w=int(input("enter the range: "))
pattern(w)