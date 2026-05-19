s={1,2,2,3,3,3,3.4,"apple"}

# 1.len()
print(len(s))
print()

# 2.remove()
s.remove(2) #removes 2 from set
print(s)
print()

# 3.pop() ==> removes a random element and returns its value
w=s.pop()
print(f"the poped element is {w}")
print(f" set aster poping {s}")
print()

# 4.clear() empty up the set
s.clear()
print(s) # prints empty set
print()

# 5. union() and intersection() and A-B abd B-A

q={1,2,3,4,5,6}
r={4,5,6,7,8,9}
print(f"q union r = {q.union(r)} \nq intersection r = {q.intersection(r)}")
print(f"q-r :{q-r}\nr-q:{r-q}")
print()