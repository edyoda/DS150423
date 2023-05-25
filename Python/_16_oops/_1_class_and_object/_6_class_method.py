class school:

    school_name = "Edyoda"  

    def __init__(self,rno,name):
        self.rno = rno
        self.name = name

    def display(self):
        print(f"Roll No. : {self.rno} \nName : {self.name} \nSchool Name : {school.school_name}")

    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
    @classmethod
    def set_school_name(cls,s_name):
        cls.school_name = s_name

obj = school("Raj",23)
obj.display()

s_name = school.get_school_name()
print("School Name : ",s_name)

school.set_school_name("Coder")

s_name = school.get_school_name()
print("School Name : ",s_name)

print(obj.get_school_name())