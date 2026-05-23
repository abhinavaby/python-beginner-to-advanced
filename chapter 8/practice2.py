#2. Write a python program using function to convert Celsius to Fahrenheit.
def con(c):
    f=(c*1.8)+32
    print(f"{c}c = {f}f")
w=float(input("enter the temp in celcius: "))
con(w)