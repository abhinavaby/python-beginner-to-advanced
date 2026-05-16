#list is mutable
#list can have multiple values assigned to a single variable
#we can access elements of list by indixing
a=[1,"abhinav",3.45,True] # example of list
print(f"{a[0]}  {a[1]} {a[2]}  {a[3]}") # display every element of array
print()
# or we can use for loop
for i in a:
    print(i)

print()
#or
for i in a:
    print(f"{i}",end=" ")