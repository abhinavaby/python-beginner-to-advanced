#1. Write a program to read the text from a given file 'f.txt' and find out whether it contains the word 'twinkle'.
c=0
r="twinkle"
f=open("f.txt","r")
w=f.readlines()
for i in range(len(w)):
    if r in w[i]:
        c+=1
        print(f"the word {r} is found in {i+1}th line")
if c==0:
    print(f"the word {r} is NOT found in practice1.txt")
else:
    print(f"the word {r} is found in the {c} lines")