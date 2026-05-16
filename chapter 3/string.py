# String can be written in three ways
a='abhinav'
b="abhinav"
c="""
a
b
h
i
n
a
v
"""
print(f"{a} {b} {c}")

# Strings are immutable(once declaired then can't be changed)

# String slicing
q='abel jones mathew'
print(f"{q[0]}+{q[1]}") #too complicated use loop instead
print()

for i in q:
    print(i)

print()

print(f"length of string {q} is {len(q)}")
print()

#slicing

w="water is good"
new_s=w[:5]
print(new_s) #print till water
new_2=w[6:] #prints is good
print(new_2)
new_3=w[6:9] #prints is 
print(new_3)

new_4=w[-4:] #prints good
print(new_4)
print()

#slicing with step value

word="amazon"
print(word[::2]) #prints aao