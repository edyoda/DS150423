# Overiding
# - overriding can only be done in inheritance
# - if parent class method implementation is not according to what we want then
#   we can override and write our own implementation

# Rules of overriding 
# 1. parent class method name and child class method name should be same
# 2. no. of parameters in child class method should be exact same with paarent class method

# when a class is not inheriting any class, then bydefault it inherits "object" class
# __str__() is object class method which returns memory address of the object of that class
# but as we don't want memory address, we override __str__() and modify it's
# implementation.

class Dad:
    def bike(self):
        print("Old Bike")

class Son(Dad):
    def bike(self):
        print("Modified Bike")

obj = Son()
obj.bike()