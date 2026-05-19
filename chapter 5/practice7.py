# If the names of 2 friends are same; what will happen to the program in problem 5?
fav_languages = {}

# First friend enters their data
fav_languages["Rahul"] = "Python"

# Second friend with the same name enters their data
fav_languages["Rahul"] = "Java" 

print(fav_languages)
# Output: {'Rahul': 'Java'}
# The dictionary only contains 3 entries instead of 4, and Rahul's language is updated to Java.
