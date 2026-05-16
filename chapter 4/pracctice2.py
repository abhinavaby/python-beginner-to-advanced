# accept 6 students mark and display it in the sorted order
mark=[]
for i in range(6):
    a=int(input(f"enter the mark of subject {i+1}: "))
    mark.append(a)
mark.sort()
print(f"the mark after sorting: {mark}")