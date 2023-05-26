# Encapsulation
 
# to access private member through public environment

# private member - canniot be accessed outside the class, to make variable/method private just add "__" as prefix

class car:

    def __init__(self,__engine,brand,mileage):
        self.__engine = __engine
        self.brand = brand
        self.mileage = mileage

    def __str__(self):
        return f"Engine : {self.__engine} \nBrand : {self.brand} \nMileage : {self.mileage}"
    
    # getter and setter
    # setter
    def set_engine(self,engine):
        self.__engine = engine

    def set_brand(self,brand):
        self.brand = brand

    def set_mileage(self,mileage):
        self.mileage = mileage

    # getter
    def get_engine(self):
        return self.__engine
    
    def get_brand(self):
        return self.brand
    
    def get_mileage(self):
        return self.mileage


obj = car("Petrol Engine","BMW","35km p/l")
print(obj,"\n")

obj.brand = "Ferrari"
# obj.__engine = "Diesel Engine"
obj.set_engine("Diesel Engine")
obj.mileage = "50km p/l"

print(obj)



