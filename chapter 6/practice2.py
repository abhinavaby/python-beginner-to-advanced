#2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
sub=[]
for i in range(3):
    w=int(input("enter the mark of subject: "))
    sub.append(w)
total=0
c=0
for i in sub:
    if(i>=33):
        c+=1
    total=total+i
per=total/(len(sub)*100)
if(c==3 and per>=40 ):
    print(f"the student have passed all subject with a overall percentage of {per}")
else:
    print(f"the student have failed with a percentage of {per}")
    

