#3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old
for i in range(2,21):
    with open(f"tables/{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i * j}\n")