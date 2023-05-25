# static / class variable
# this variable is declared inside the class and outside the method/constructor
# scope - throughout the class
# are used for memory management
# it shares the same memory

address = "Mumbai"

class school:

    school_name = "Edyoda"   # class / static variable

    def __init__(self,rno,name):
        self.rno = rno
        self.name = name
        self.school_name = "Coder"

    def display(self):
        print(f"Roll No. : {self.rno} \nName : {self.name} \nSchool Name : {school.school_name} {self.school_name}")


obj = school("Raj",23)
obj.display()

obj1 = school("Ram",24)
obj1.display()
print(obj1.school_name)