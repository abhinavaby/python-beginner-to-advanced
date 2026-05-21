#1. Write a program to find the greatest of four numbers entered by the user.
l=[]
for i in range(4):
    w=int(input(f"enter the {i+1} number: "))
    l.append(w)
greatest=l[0]
for i in l:
    if(greatest<i):
        greatest=i

print(f"the grestest number is {greatest}")
