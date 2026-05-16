#string methods will return a new sting but list method change is done on the same list


# 1.append()

a=["abhinav","rohan","abel","amal"]
a.append("albin")
a.append(2)
print(a)
print()

# 2.sort()

b=[2,1,3,5,4,6,8,7,9]
b.sort()
print(b)
print()

# 3. reverse()
c=[2,1,3,5,4,6,8,7,9]
c.reverse()
print(c)

# 4. insert()

d=[2,1,3,5,4,6,8,7,9]
d.insert(0,10) # inserts 10 at 0th index
print(d)
print()

# 5. pop()

w=[2,1,3,5,4,6,8,7,9]
w.pop(1) #deletes element at index 1
print(w)

# 6.remove()

e=[2,1,3,5,4,6,8,7,9,9]
e.remove(9) # remove the first occuring 9 from list 
print(e)
print()
# to remove all 9

r=[2,1,3,5,4,6,8,7,9,9]
print(f"before: {r}")
while 9 in r:
    r.remove(9)
print(f"after: {r}")
print()
print()


#-------------from LLM-------------------# 


# Initialize a starting list
languages = ["Python", "Java", "C++"]
print(f"Original list: {languages}")

# 1. ADDING ELEMENTS
languages.append("JavaScript")          # Adds to the very end
languages.insert(1, "Ruby")             # Inserts 'Ruby' at index 1
languages.extend(["Go", "Rust"])        # Appends multiple items from another list
print(f"After adding elements: {languages}")

# 2. SEARCHING & COUNTING
languages.append("Python")              # Add a duplicate for counting
python_count = languages.count("Python") # Counts occurrences of 'Python'
java_index = languages.index("Java")     # Finds the index of 'Java'
print(f"'Python' appears {python_count} times. 'Java' is at index {java_index}.")

# 3. REMOVING ELEMENTS
removed_item = languages.pop()          # Removes and returns the last item
languages.remove("Ruby")                # Removes the first occurrence of 'Ruby'
del languages[0]                        # Alternative: deletes item at index 0
print(f"Removed last item: '{removed_item}'")
print(f"After removals: {languages}")

# 4. ORDERING & SORTING
languages.sort()                        # Sorts alphabetically/numerically in place
print(f"Sorted list: {languages}")

languages.reverse()                     # Reverses the order in place
print(f"Reversed list: {languages}")

# 5. COPYING & CLEARING
list_copy = languages.copy()            # Creates a shallow copy of the list
languages.clear()                       # Empties the entire list
print(f"Original list after clear(): {languages}")
print(f"The independent copy remains: {list_copy}")
