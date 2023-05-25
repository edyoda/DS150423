# Constructor
# constructor are special methods
# it is defined with the name __init__()
# it gets called automatically when object is created
# it is use to create object
# it is use to initialize instance variable
# it doesnot have a return statement

# NOTE : It is not recommended to write logic in constructor

# class python:

#     def __init__(self):              # constructor
#         self.n1 = 0
#         self.n2 = 0

#     def getinput(self):                            # instance method
#         self.n1 = int(input('Enter no1:   '))
#         self.n2 = int(input('Enter no2:   '))

#     def addition(self):
#         return self.n1 + self.n2

# obj = python()                      # calling construtor
# obj.getinput()
# res = obj.addition()
# print("Result : ",res)


# Types of Constructor
# 1. Default Constructor - when you don't have constructor in your class, then pvm provides the default constructor
# 2. Zero Constructor    - constructor with no parameters
# 3. Parameterized Constructor - constructor with parameters

class student:

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def display(self):
        print("Name: ",self.name)
        print("Roll No: ",self.rno)

student_obj = student("Bharati",90)
student_obj.display()
