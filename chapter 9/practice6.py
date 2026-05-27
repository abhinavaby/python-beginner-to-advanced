
#6. Write a program to find the line number where donkey is present from ques 5.
with open("f3.txt","r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if("donkey" in lines[i]):
            print(f"the line number where donkey is present is:{i+1}")