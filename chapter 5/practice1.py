# Write a program to input eight numbers from the user and display all the unique numbers (once)
s=set()
for i in range(8):
    w=int(input(f"enter the {i+1} number: "))
    s.add(w)
print(f"unique numbers={s}")
print()
print("or")
print()
print("unique numbers: ")
for i in s:
    print(i,end=" ")
