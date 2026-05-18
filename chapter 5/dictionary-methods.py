mark = {
    "abhinav": 10,
    "abel": 23,
    "jacob": 55,
    0:"rahul"
}

# 1.items()

a=mark.items() # return list inside tuples
print(f"keys and values= {a}")
for i in a:
    print(i) # prints each tuple
print()
    # 2.keys()

b=mark.keys() # returns list of of string keys
print(f"keys = {b}")
for i in b:
    print(i)
print()

# 3.values()
c=mark.values()
print(f"values = {c}")
for i in c:
    print(i)
print()

# 4.update()

mark.update({"abhinav":9,"ashik":100}); # updates alrady existing data and add the rest(non existing data) to the dictionary as it is mutable


print(mark)
print()

# 5 .get()
f=mark.get("abhinav")
r=mark["abhinav"]
print(f)
print(r)
f=mark.get("abhinav1") #returns None if the key doesnot exist 
# r=mark["abhinav1"] # returns error if the key doesnot exist
print(f)
print()
print()



#---------------------from LLM-----------------------
# 1. Setup a baseline dictionary
student = {"name": "Abhinav", "age": 21, "course": "Python"}

# 2. Key Retrieval Methods
print(student.get("name"))              # 'Abhinav' (Safe lookup)
print(student.get("grade", "N/A"))     # 'N/A' (Fallback value if key is missing)
print(list(student.keys()))             # ['name', 'age', 'course'] (Get keys)
print(list(student.values()))           # ['Abhinav', 21, 'Python'] (Get values)
print(list(student.items()))            # [('name', 'Abhinav'), ...] (Get pairs)

# 3. Modification & Insertion Methods
student.update({"age": 22, "city": "Kozhikode"}) # Updates 'age' and adds 'city'
student.setdefault("status", "Active")           # Adds 'status' since it doesn't exist
student.setdefault("name", "Guest")              # Changes nothing because 'name' exists

# 4. Deletion Methods
age_value = student.pop("age")          # Removes 'age' and returns 22
last_item = student.popitem()           # Removes and returns last pair: ('status', 'Active')

# 5. Copying and Clearing Methods
backup = student.copy()                 # Creates a shallow copy
student.clear()                         # Empties the dictionary -> {}

# Print final states to verify
print("Student:", student)              # Output: {}
print("Backup:", backup)                # Output: {'name': 'Abhinav', 'course': 'Python', 'city': 'Kozhikode'}

