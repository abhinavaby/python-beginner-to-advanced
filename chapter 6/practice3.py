#3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
l = ["Make a lot of money", "buy now", "subscribe this", "click this"]
a = input("enter a comment: ")

# Flag to track if we found spam
is_spam = False

# Loop through each keyword to see if it is inside the comment
for keyword in l:
    if keyword in a:
        is_spam = True
        break  # Stop checking once spam is found

if is_spam:
    print("its a spam comment")
else:
    print("not a spam comment")
