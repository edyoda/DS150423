class laptop:

    def __init__(self,motherboard,brand,memory):
        self.motherboard = motherboard
        self.brand = brand
        self.memory = memory

    #setters and getters
    def get_motherboard(self):
        return self.motherboard
    
    def set_motherboard(self,motherboard):
        self.motherboard = motherboard

    def get_brand(self):
        return self.brand
    
    def set_brand(self,brand):
        self.brand = brand

    def get_memory(self):
        return self.memory
    
    def set_memory(self,memory):
        self.memory = memory

    def display(self):
        return f"Motherboard : {self.motherboard} \nBrand : {self.brand} \nMemory : {self.memory}"
    
obj = laptop("Gigabyte","Dell","8GB")
print(obj.display())



obj.set_motherboard("Asus")
print(obj.get_motherboard())


obj.set_brand("HP")
print(obj.get_brand())

obj.set_memory("16GB")
print(obj.get_memory())


