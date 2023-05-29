# class Grandpa:
#     def field(self):
#         print("Field")

# class Dad(Grandpa):
#     def flat(self):
#         print("Flat")

# class Son(Dad):
#     def bike(self):
#         print("Bike")

# class Grandson(Son):
#     def mobile(self):
#         print("Mobile")

# grandson = Grandson()
# grandson.mobile()
# grandson.bike()
# grandson.flat()
# grandson.field()




class grandpa:
    def old_bike(self):
        print('Rajdoot ---> belong to Grandpa')

class dad(grandpa):
    def flat(self):
        print('Gokul Hieghts 103 ---> belongs to Dad')

class son(dad):
    def car(self):
        print('Maruti 800 ---> belongs to Son')

class grandson(son):
    def what(self):
        print('Has nothing of his own, all inherited stuff only')

obj = grandson()
obj.what()
obj.car()
obj.flat()
obj.old_bike()

# Multilevel
class input1 - function which takes one parameter
class input2 - function which takes 2nd parameter
class addition - function which adds both one and 2nd parameter