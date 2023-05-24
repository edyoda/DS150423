# instance variable
# it is defined inside the class
# instance variable are defined as "self." as prefix i.e. self.<variable_name>
# scope - throughout the class

class calculator:
    def getinput(self):                            # instance method
        self.n1 = int(input('Enter no1:   '))
        self.n2 = int(input('Enter no2:   '))

    def addition(self):
        return self.n1 + self.n2
    
obj = calculator()
# obj.getinput()
result = obj.addition()
print(result)
obj.n1 = 90
print(obj.n1)
