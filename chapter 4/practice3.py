# sum of list elements
l=[]
for i in range(4):
    a=int(input("enter the number: "))
    l.append(a)
sum=03
for i in l:
    sum+=i
print(f"the list : {l}")
print(f"sum of elements: {sum}")