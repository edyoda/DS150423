class College:
    def __init__(self,college_name,college_address):
        self.college_name = college_name
        self.college_address = college_address

class Student(College):
    def __init__(self,rno,name,college_name,college_address):
        super().__init__(college_name,college_address)
        self.rno = rno
        self.name = name

    def __str__(self):
        return f"College Name : {self.college_name} \nCollege Address : {self.college_address} \nRno : {self.rno} \nName : {self.name}"
    
student = Student(1,"Raj","Edyoda","Bangalore")
print(student)
