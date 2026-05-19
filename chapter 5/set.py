s={} #empty dictionary
s1={1,2,3,4} #set
e=set() #emprty set 

#sets are unordered





# elements doesnot repeat in set 
q={1,2,2,2,3,4,5,5,5,"rohan",True,3.55} 
print(q) #elements are not repeated and order is not maintained 




#-----------------from LLM-------------------------

# 1. Setup baseline sets
fruits = {"apple", "banana", "cherry"}
berries = {"strawberry", "raspberry", "cherry"}

# 2. Modification Methods (Add / Remove)
fruits.add("orange")               # Adds 'orange' to the set
fruits.remove("banana")            # Removes 'banana' (Raises KeyError if missing)
fruits.discard("grape")            # Safely removes 'grape' (Does nothing if missing)
popped_item = fruits.pop()         # Removes and returns an arbitrary element

# 3. Mathematical Operations (Create new sets)
union_set = fruits.union(berries)               # Combines both sets (All unique items)
intersect_set = fruits.intersection(berries)   # Items present in both sets
diff_set = fruits.difference(berries)           # Items in fruits but not in berries
sym_diff = fruits.symmetric_difference(berries) # Items in either set, but not both

# 4. In-Place Mathematical Operations (Modify the original set)
fruits.intersection_update(berries) # Keeps only items found in both sets

# 5. Relationship Evaluation (Returns True/False)
is_disjoint = fruits.isdisjoint(berries)  # True if sets share zero common elements
is_subset = fruits.issubset(berries)      # True if all fruits elements are in berries
is_superset = berries.issuperset(fruits)  # True if berries contains all fruits elements

# 6. Copying and Clearing Methods
fruits_copy = fruits.copy()        # Creates a shallow copy
fruits.clear()                     # Empties the set -> set()



print()


# 1. Setup baseline sets
numbers_a = {1, 2, 3, 4, 5}
numbers_b = {4, 5, 6, 7, 8}

# 2. Modification Methods (Add / Remove)
numbers_a.add(6)                   # {1, 2, 3, 4, 5, 6} (Adds 6)
numbers_a.remove(2)                # {1, 3, 4, 5, 6} (Removes 2; errors if missing)
numbers_a.discard(99)              # {1, 3, 4, 5, 6} (Safely skips missing 99)
popped_num = numbers_a.pop()       # Removes and returns an arbitrary number

# Resetting sets for mathematical examples
set_x = {1, 2, 3}
set_y = {3, 4, 5}

# 3. Mathematical Operations (Returns a new set)
print(set_x.union(set_y))                  # {1, 2, 3, 4, 5} (All unique items)
print(set_x.intersection(set_y))           # {3} (Elements in both)
print(set_x.difference(set_y))             # {1, 2} (Elements in set_x but not set_y)
print(set_x.symmetric_difference(set_y))   # {1, 2, 4, 5} (Elements in either, but not both)

# 4. In-Place Operations (Modifies the original set)
set_x.intersection_update(set_y)           # set_x becomes {3}

# 5. Relationship Evaluation (Returns True or False)
small_set = {1, 2}
large_set = {1, 2, 3, 4}

print(small_set.issubset(large_set))       # True (All elements of small are in large)
print(large_set.issuperset(small_set))     # True (Large contains all elements of small)
print(small_set.isdisjoint({5, 6}))        # True (They share no common elements)

# 6. Copying and Clearing
set_copy = large_set.copy()                # Creates a separate copy {1, 2, 3, 4}
large_set.clear()                          # Empties the set -> set()

print()





# 1. Setup baseline numerical sets
set_x = {1, 2, 3}
set_y = {3, 4, 5}

# 2. Mathematical Shorthand Operators (Returns a new set)
union_set = set_x | set_y                # {1, 2, 3, 4, 5} (Pipe symbol for Union)
intersect_set = set_x & set_y            # {3} (Ampersand for Intersection)
diff_set = set_x - set_y                # {1, 2} (Minus sign for Difference)
sym_diff = set_x ^ set_y                # {1, 2, 4, 5} (Caret for Symmetric Difference)

# 3. In-Place Shorthand Operators (Modifies the original left-side set)
set_x |= set_y                           # set_x becomes {1, 2, 3, 4, 5} (Union Update)
set_x &= {3, 4}                          # set_x becomes {3, 4} (Intersection Update)
set_x -= {4}                             # set_x becomes {3} (Difference Update)
set_x ^= {3, 9}                          # set_x becomes {9} (Symmetric Difference Update)

# 4. Comparison Operators for Relationships (Returns True or False)
small = {1, 2}
large = {1, 2, 3, 4}

print(small < large)                     # True (Strict subset: small is inside large and not equal)
print(small <= large)                    # True (Subset evaluation)
print(large > small)                     # True (Strict superset evaluation)
print(large >= small)                    # True (Superset evaluation)
print(small == {2, 1})                   # True (Equality evaluation ignores order)






