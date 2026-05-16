a="""
    hi <name>
    you got <mark>
    congrats"""
q=input("enter your name: ")
w=input("enter your marks: ")
print(a.replace("<name>",q).replace("<mark>",w)) #first a.replace("<name>",q) returns a string that only 
                                                 #changes the the name but a.replace("<name>",q).replace("<mark>",w) this 
                                                 # changes both name and mark , this is called chaining