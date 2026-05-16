# 1.len()
a="abhinav"
q=len(a)
print(f"length of {a} is {q}")
print()

# 2.endswith()

print(a.endswith("inav")) # returns True or False
print()

# 3.startwith()

print(a.startswith("abh")) # returns True or False
print()

# capitalize()
print(a.capitalize())
print()




#---------------------from LLM---------------------------
text = "  python programming is fun!  "

# 1. strip() - Removes leading and trailing whitespace
clean_text = text.strip()
print(f"strip(): '{clean_text}'")

# 2. lower() & upper() - Converts case
print(f"lower(): '{clean_text.lower()}'")
print(f"upper(): '{clean_text.upper()}'")

# 3. title() - Capitalizes first letter of each word
print(f"title(): '{clean_text.title()}'")

# 4. replace() - Replaces a substring with another
replaced = clean_text.replace("fun", "awesome")
print(f"replace(): '{replaced}'")

# 5. split() - Splits string into a list based on a delimiter
words = clean_text.split(" ")
print(f"split(): {words}")

# 6. join() - Joins list elements into a single string
joined = "-".join(words)
print(f"join(): '{joined}'")

# 7. find() - Returns lowest index of substring, or -1 if not found
index = clean_text.find("prog")
print(f"find('prog'): {index}")

# 8. startswith() & endswith() - Checks start/end characters (returns Boolean)
print(f"startswith('py'): {clean_text.startswith('py')}")
print(f"endswith('!'): {clean_text.endswith('!')}")

# 9. isdigit() - Checks if string contains only digits
num_str = "12345"
print(f"isdigit() on '12345': {num_str.isdigit()}")

# 10. len() - Returns total character count (built-in function used on strings)
print(f"len(): {len(clean_text)}")
