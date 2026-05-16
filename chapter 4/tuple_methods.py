# 1.count() => returns the count of the element
a=(10,34.44,"rohan",True,True)
b=a.count(True) # as string and tuple are immutable we cant change the original string or tuple , when we use this function a string or tuple is returned
print(b)
print()


#-------------------from LLM---------------------------

# Initialize a starting tuple with some duplicate elements
coordinates = (10, 20, 30, 20, 40, 20)
print(f"Original tuple: {coordinates}")

# 1. THE count() METHOD
# Returns the total number of times a specific value appears in the tuple
count_of_20 = coordinates.count(20)
print(f"The number 20 appears {count_of_20} times.")

# 2. THE index() METHOD
# Returns the index position of the FIRST occurrence of a specific value
# Raises a ValueError if the item is not found in the tuple
index_of_30 = coordinates.index(30)
index_of_first_20 = coordinates.index(20) # Finds the first one, ignoring later duplicates

print(f"The number 30 is located at index {index_of_30}.")
print(f"The first occurrence of 20 is at index {index_of_first_20}.")

# BONUS: Useful built-in functions that work with tuples (but are not tuple methods)
print(f"Total elements (len): {len(coordinates)}")
print(f"Highest value (max): {max(coordinates)}")
print(f"Lowest value (min): {min(coordinates)}")
print(f"Sum of elements (sum): {sum(coordinates)}")


print()
# Initialize a base tuple representing a user profile
# Format: (ID, First Name, Last Name, Role, City, Country, Status)
user_profile = (101, "Alice", "Smith", "Developer", "New York", "USA", "Active")
print(f"Original Tuple: {user_profile}\n")

# ==========================================
# 1. TUPLE SLICING Examples [start:stop:step]
# ==========================================

# Extract elements from index 1 up to (but not including) index 4
name_and_role = user_profile[1:4]
print(f"Slicing [1:4] (Name & Role): {name_and_role}")

# Extract everything from index 4 to the very end
location = user_profile[4:]
print(f"Slicing [4:] (Location details): {location}")

# Reverse the entire tuple using a negative step
reversed_tuple = user_profile[::-1]
print(f"Slicing [::-1] (Reversed): {reversed_tuple}\n")


# ==========================================
# 2. TUPLE UNPACKING Examples
# ==========================================

# Standard Unpacking: Variables must match the exact number of elements
short_tuple = ("Python", "3.12")
language, version = short_tuple
print(f"Standard Unpacking: {language} version {version}")

# Extended Unpacking: Using the asterisk (*) operator to capture remaining items
user_id, first_name, last_name, *professional_details = user_profile
print(f"Unpacked ID: {user_id}")
print(f"Unpacked Name: {first_name} {last_name}")
print(f"Captured leftover items into a list (*): {professional_details}")

# Ignore values using underscore (_) placeholders
_, current_fname, _, _, _, native_country, _ = user_profile
print(f"Targeted Unpacking (using _ to ignore others): {current_fname} from {native_country}")

