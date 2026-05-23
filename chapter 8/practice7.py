def s(w):
    q = input("enter the letter to remove: ")
    
    # 1. To show the word as a list with the letter removed:
    a = list(w)
    if q in a:
        a.remove(q)  # Removes the first occurrence
    
    # 2. To remove all occurrences from the string:
    r = w.replace(q, "") 
    
    print(a)
    print(r)

v = input("enter the string: ")
s(v)
