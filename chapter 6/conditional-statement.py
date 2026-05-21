# if anycondition is met da a certain thing 


#if else

a=int(input("enter the age: "))
if a >= 18:
    print("you are eligibe for voting......")
else:
    print("you cant vote.........")
print("end of program")


#if else elif

a=int(input("enter the age: "))
if a >= 18:
    print("you are eligibe for voting......")
elif(a>100 and a<0):
    print("you entered an invalid age......")
else:
    print("you cant vote.........")
print("end of program")

