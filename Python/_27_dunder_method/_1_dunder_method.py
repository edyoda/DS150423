# Dunder Method | Special Method | Magic Method

# __init__ - create object
# __str__ - print obj
# __mro__ - mro()
# __add__

# print(dir(list))

# no1 = 10
# no2 = 20
# add = no1 + no2
# print(add)

class special_method:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name}'s salary is 4{self.salary}"
    
    def __len__(self):
        return len(self.name) # __len__ --> Guido
    
    def __add__(self,self1):
        return self.salary + self1.salary
    
    def __mul__(self,self1):
        return self.salary * self1.salary
    
    
obj1 = special_method("Ram",10000)
obj2 = special_method("Raj",20000)
print(obj1)

print(len(obj1)) # __len__ --> Bharati

print(obj1 + obj2)

print(obj1 * obj2)