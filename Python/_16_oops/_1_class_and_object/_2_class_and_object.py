# self 
# keyword
# it's a mandatory parameter in every method
# self represents the current class object

class calculator:
    def getinput(self):
        n1 = int(input('Enter no1:   '))
        n2 = int(input('Enter no2:   '))
        return n1, n2

    def addition(self,num1, num2):
        return num1 + num2
    
obj = calculator()
num1, num2 = obj.getinput()
result = obj.addition(num1, num2)
print(result)


