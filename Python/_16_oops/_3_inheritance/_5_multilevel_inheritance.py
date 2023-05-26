# class Input1:
#     def __init__(self, param1):
#         self.param1 = param1

# class Input2(Input1):
#     def __init__(self, param1, param2):
#         super().__init__(param1)
#         self.param2 = param2

# class Addition(Input2):
#     def __init__(self, param1, param2):
#         super().__init__(param1, param2)

#     def add(self):
#         return self.param1 + self.param2
    
# input1 = Input1(10)
# input2 = Input2(20, 30)
# addition = Addition(40, 50)

# print(addition.add())



class input1:
    def number1(self, no1):
        self.no1 = no1
        # return self.no1
    
class input2(input1):
    def number2(self, no2):
        self.no2 = no2
        # return self.no2
    
class addition(input2):
    def summation(self):
        addn = self.no1 + self.no2
        return addn
    

obj = addition()
obj.number1(20)
obj.number2(40)
result = obj.summation()
print(f'Sum of the numbers is {result}')