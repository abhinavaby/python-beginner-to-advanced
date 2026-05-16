""" adding fruits name to list by the user """
print("enter exit to break")
print()
l=[]
while True:
    a=input("enter the fruit name: ")
    if a=="exit":
        break
    else:
        l.append(a)
print(f"the list is : {l}")