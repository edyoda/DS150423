# Encapsulation
 
# it is use to bind attributes (varibles) and behaviuour (methods) together into single unit
# to access private member through public environment

class car:

    def __init__(self,engine,brand,mileage):
        self.engine = engine
        self.brand = brand
        self.mileage = mileage

    def display(self):
        return f"Engine : {self.engine} \nBrand : {self.brand} \nMileage : {self.mileage}"
    
    # getter and setter
    # setter
    def set_engine(self,engine):
        self.engine = engine

    def set_brand(self,brand):
        self.brand = brand

    def set_mileage(self,mileage):
        self.mileage = mileage

    # getter
    def get_engine(self):
        return self.engine
    
    def get_brand(self):
        return self.brand
    
    def get_mileage(self):
        return self.mileage


    

obj = car("Petrol Engine","BMW","35km p/l")
data = obj.display()
print(data)

obj.set_engine("Diesel Engine")
obj.set_mileage("50km p/l")
data = obj.display()
print(data)

print("Engine : ",obj.get_engine())
print(obj.get_brand())
print(obj.get_mileage())


# class - laptop
# attributes - motherboard, brand, memory