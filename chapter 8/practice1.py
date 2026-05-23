#1. Write a program using functions to find greatest of three numbers.
def gre(a):
    gr=a[0]
    for i in a:
        if(i>gr):
            gr=i
    return gr
w=[]
for i in range(3):
    q=int(input("enter the number: "))
    w.append(q)

print(f"greates of three numbers = {gre(w)}")
