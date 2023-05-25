class school:

    def __init__(self,rno,name):
        self.rno = rno
        self.name = name

    def display(self):
        print(f"Roll No. : {self.rno} \nName : {self.name}")

    @staticmethod
    def static_method():
        return "Hey All"

obj = school("Raj",23)
obj.display()
print(school.static_method())
print(obj.static_method())

