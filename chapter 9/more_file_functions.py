f=open("file3.txt")
w=f.readlines() #returns list (eg==>['hi guys\n', 'this is abhinav here\n', 'how are you'] )
print(w,type(w))
f.close()

#reading line by line

f=open("file3.txt")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
line4=f.readline()
print(line4)


print(line4=="") #means line 4 is empty, that is there is no line 4
f.close()

print()
print("using loop")


#reading line by line using loop
f=open("file3.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()

