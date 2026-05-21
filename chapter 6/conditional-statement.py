# if anycondition is met da a certain thing 


#if else

a=int(input("enter the age: "))
if a >= 18:
    print("you are eligibe for voting......")
else:
    print("you cant vote.........")
print("end of program")
print("\n\n")


#if else elif ladder

a=int(input("enter the age: "))

if(a>100 or a<0):
    print("you entered an invalid age......")
elif( a >= 18):
    print("you are eligibe for voting......")
else:
    print("you cant vote.........")
print("end of program")

