#7. Write a program to make a copy of a text file "this. txt"
with open("f2.txt","r") as f2:
    read=f2.read()
with open("copy.txt","w") as f3:
    f3.write(read)