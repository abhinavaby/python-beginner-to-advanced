# give a piece of logic as name
 #eg(avg of 3 numbers)

def avg(a,b,c):
    return (a+b+c)/3
print(f"enter 00 to exit")

while True:
    a=int(input("enter the number: "))
    if(a==00):
        break
    b=int(input("enter the number: "))
    if(b==00):
        break
    a
    c=int(input("enter the number: "))
    if(c==00):
        break
    av=avg(a,b,c)
    print(f"average of {a},{b},{c} is {av}")
print()

# function without parameters

def hi():
    print("hi.......")

hi()
hi()
hi()  # prints hi three times


