s="\nhow are you?"
f=open("f.txt","a")
f.write(s)
f.close() #how many times we will print that much time it wil be added


#with statement
with open("f.txt","r") as f:
    print(f.read())
#here no need to close the file