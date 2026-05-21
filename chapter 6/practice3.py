#3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
l=["Make a lot of money", "buy now", "subscribe this", "click this"]
a=input("enter a comment: ")
if( a in l ):
    print("its a spam comment")
else:
    print("not a spam comment")
