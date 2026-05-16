#list are mutable

a=["abhinav","rohan","abel","amal"]
# changing rohan to david
for i in range(len(a)):
    if a[i]=="rohan":
        a[i]="david"
print(a)

#slicig (just like string)
print()
print(a[:2])
