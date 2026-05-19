# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d={}
for i in range(4):
    w=input("enter your name: ")
    e=input("enter your fav language: ")
    d[w]=e
print(f"dictionary:{d}")