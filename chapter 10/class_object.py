
#first program
class employee: #act as template
    name = "harry"
    language = "py"
    salary=123333
a=employee() #here a is a object
print(a.name,a.language,a.salary)   

print()
print()

class employe: #act as template
    
    language = "py" #class attributes
    salary=123333 #class attributes

rohan=employe() #here a is a object
rohan.name="rohan reji" #object attribute or instence attribute
print(rohan.language,rohan.salary,rohan.name)

jacob=employe()
jacob.name="jacob boy" #object attribute or instence attribute
print(jacob.language,jacob.salary,jacob.name)

#here name is object attribute and salary and language are class attributes as they directly belong to the class

print()
print()

# ==========================================
# CLASS: The Blueprint / Template
# ==========================================
class MobilePhone:
    # Class Attribute (Shared by all instances)
    device_category = "Communication"

    # Constructor Method (Initializes unique instance properties)
    def __init__(self, brand, model, battery_level):
        self.brand = brand                  # Instance Attribute
        self.model = model                  # Instance Attribute
        self.battery = battery_level        # Instance Attribute

    # Instance Method (Defines the object's behavior)
    def charge(self):
        self.battery = 100
        return f"The {self.brand} {self.model} is now fully charged."


# ==========================================
# OBJECTS: The Real Instances Built From Class
# ==========================================

# object_1 is a distinct instance with its own data
object_1 = MobilePhone(brand="Apple", model="iPhone 15", battery_level=45)

# object_2 is a separate instance with completely different data
object_2 = MobilePhone(brand="Google", model="Pixel 8", battery_level=80)


# ==========================================
# USAGE: Interacting with Objects
# ==========================================

# 1. Accessing object properties (Attributes)
print(object_1.brand)          # Output: Apple
print(object_2.battery)        # Output: 80

# 2. Triggering object actions (Methods)
print(object_1.charge())       # Output: The Apple iPhone 15 is now fully charged.
print(object_1.battery)        # Output: 100 (Battery level was updated)

# 3. Verifying shared class data
print(object_2.device_category) # Output: Communication
