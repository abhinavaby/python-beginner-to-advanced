#5. Repeat program 4 for a list of such words to be censored.
w=["lion","tiger"]
with open("f3.txt",'r') as f:
    e=f.read()
with open("f3.txt",'w') as f:
    for i in w:
        e=e.replace(i,"#"*len(i))
    f.write(e)