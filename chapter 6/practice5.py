#5. Write a program which finds out whether a given name is present in a list or not.
l=[]
for i in range(5):
    w=input("enter a name: ")
    l.append(w)
c=input("enter the name: ")
if(c in l):
    print("name in list")
else:
    print("name not in list")