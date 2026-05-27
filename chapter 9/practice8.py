#8. Write a program to find whether a file is identical & matches the content of another file.
with open("copy.txt","r") as f2:
    read=f2.read()
with open("f2.txt","r") as f3:
    read2=f3.read()
if read==read2:
    print("these two files are same")
else:
    print("these two files are different")

