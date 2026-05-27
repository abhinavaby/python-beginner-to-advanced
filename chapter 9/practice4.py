#4. A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("f2.txt","r") as f2:
    lines = f2.readlines()

with open("f2.txt","w") as f2:
    for i in lines:
        w=i.replace("donkey","######")
        f2.write(w)