#6. Write a python function which converts inches to cms.
def con(i):
    c=i*2.54
    print(f"{i}inch = {c}cms")
w=float(input("enter the measurement in inch: "))
con(w)    